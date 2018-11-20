# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StoneScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EmpresaItem(scrapy.Item):
    atividade_principal = scrapy.Field()
    data_situacao  = scrapy.Field()
    complemento = scrapy.Field()
    nome = scrapy.Field()
    uf = scrapy.Field()
    telefone = scrapy.Field()
    email = scrapy.Field()
    atividades_secundarias = scrapy.Field()
    qsa = scrapy.Field()
    situacao = scrapy.Field()
    bairro = scrapy.Field()
    logradouro = scrapy.Field()
    numero = scrapy.Field()
    cep = scrapy.Field()
    municipio = scrapy.Field()
    abertura = scrapy.Field()
    natureza_juridica = scrapy.Field()
    fantasia = scrapy.Field()
    cnpj = scrapy.Field()
    ultima_atualizacao = scrapy.Field()
    status = scrapy.Field()
    tipo = scrapy.Field()
    efr = scrapy.Field()
    motivo_situacao = scrapy.Field()
    situacao_especial = scrapy.Field()
    data_situacao_especial = scrapy.Field()
    capital_social = scrapy.Field()
    extra = scrapy.Field()
    billing = scrapy.Field()
