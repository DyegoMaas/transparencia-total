# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity


class DeputadoItem(scrapy.Item):
    id = scrapy.Field()
    nome = scrapy.Field()
    biografia = scrapy.Field()
    url_foto = scrapy.Field()
    partido = scrapy.Field()
    cargo_mesa_diretora = scrapy.Field()
    lider_no_bloco = scrapy.Field()
    vice_no_bloco = scrapy.Field()


class DeputadoLoader(ItemLoader):
    default_output_processor = TakeFirst()
    biografia_out = Identity()


class GastoCusteadoItem(scrapy.Item):
    tipo = scrapy.Field()
    periodo = scrapy.Field()
    nome_deputado = scrapy.Field()
    descricao = scrapy.Field()
    valor = scrapy.Field()
    data = scrapy.Field()
    url_pdf = scrapy.Field()
    file_urls = scrapy.Field()


class GastoCusteadoLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ProjetoLeiItem(scrapy.Item):
    document_url = scrapy.Field()
    status = scrapy.Field()
    descricao = scrapy.Field()
