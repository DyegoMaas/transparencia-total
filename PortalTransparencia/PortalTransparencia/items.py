# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity


class DeputadoFederalItem(scrapy.Item):
    id = scrapy.Field()
    nome = scrapy.Field()
    biografia = scrapy.Field()
    url_foto = scrapy.Field()
    partido = scrapy.Field()
    cargo_mesa_diretora = scrapy.Field()
    lider_no_bloco = scrapy.Field()
    vice_no_bloco = scrapy.Field()


class DeputadoFederalLoader(ItemLoader):
    default_output_processor = TakeFirst()

    biografia_out = Identity()
    # name_in = MapCompose(unicode.title)
    # name_out = Join()

    # price_in = MapCompose(unicode.strip)


class GastoCusteadoItem(scrapy.Item):
    descricao = scrapy.Field()
    valor = scrapy.Field()
    data = scrapy.Field()
    nome_deputado = scrapy.Field()


class ProjetoLeiItem(scrapy.Item):
    document_url = scrapy.Field()
    status = scrapy.Field()
    descricao = scrapy.Field()
