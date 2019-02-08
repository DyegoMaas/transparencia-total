# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from .. items import GastoCusteadoItem, GastoCusteadoLoader


class DeputadosEstaduaisParanaCusteiosSpider(scrapy.Spider):
    name = 'deputados_estaduais_pr_custeios'
    allowed_domains = ['alep.pr.gov.br']
    start_urls = ['http://www.alep.pr.gov.br/transparencia/fiscalize/verbas-de-ressarcimento/']

    def parse(self, response):
        periodos = response.css('#select-date option')
        for periodo in periodos:
            identificador = periodo.css('::attr(value)').extract_first()
            descricao_data = periodo.css('::text').extract_first()

            url = response.urljoin('/transparencia/ajax?ID={id}'.format(id=identificador))
            meta = {'periodo': descricao_data}
            yield Request(url, meta=meta, callback=self.parse_custeio_mes)
            break

    def parse_custeio_mes(self, response):
        periodo = response.meta['periodo']

        links = response.css('a')
        for link in links:
            text = link.css('::text')
            tipo = text.re('(.*) \(.*')[0]
            nome_deputado = text.re('.* \((.*)\)')[0]
            url_pdf = link.css('::attr(href)').extract_first()

            print('tipo: {0}'.format(tipo))

            custeio = GastoCusteadoLoader(item=GastoCusteadoItem())
            custeio.add_value('tipo', tipo)
            custeio.add_value('periodo', periodo)
            custeio.add_value('nome_deputado', nome_deputado)
            custeio.add_value('url_pdf', url_pdf)
            custeio.add_value('file_urls', url_pdf)
            yield custeio.load_item()
