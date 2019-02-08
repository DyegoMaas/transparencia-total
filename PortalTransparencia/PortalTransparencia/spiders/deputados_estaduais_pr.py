# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .. items import DeputadoLoader, DeputadoItem

class DeputadosEstaduaisParanaSpider(CrawlSpider):
    name = 'deputados_estaduais_pr'
    allowed_domains = ['alep.pr.gov.br']
    start_urls = ['http://www.alep.pr.gov.br/deputados']

    rules = (
        Rule(LinkExtractor(allow='perfil/'), callback='parse_deputado'),
    )

    def parse_deputado(self, response):
        deputado = DeputadoLoader(item=DeputadoItem(), response=response)
        deputado.add_css('nome', '.nome-deputado::text')
        deputado.add_css('biografia', 'div.bio span::text')
        deputado.add_value('partido', response.css('.contato p.partido::text').re('.*- (.*)'))
        deputado.add_css('url_foto', 'figure.imagem img::attr(src)')

        return deputado.load_item()
