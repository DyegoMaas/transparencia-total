# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .. items import DeputadoFederalLoader, DeputadoFederalItem

class DeputadosSpider(CrawlSpider):
    name = 'deputados_federais'
    allowed_domains = ['alep.pr.gov.br']
    start_urls = ['http://www.alep.pr.gov.br/deputados']

    rules = (
        Rule(LinkExtractor(allow=r'deputados/perfil/'), callback='parse_deputado', follow=True),
    )

    def parse_deputado(self, response):
        deputado = DeputadoFederalLoader(item=DeputadoFederalItem(), response=response)
        deputado.add_css('nome', '.nome-deputado::text')
        deputado.add_css('biografia', 'div.bio span::text')
        deputado.add_value('partido', response.css('.contato p.partido::text').re('.*- (.*)'))
        deputado.add_css('url_foto', 'figure.imagem img::attr(src)')

        return deputado.load_item()
