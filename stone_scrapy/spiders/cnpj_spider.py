import scrapy
import json
from os import path
from stone_scrapy.items import EmpresaItem

class CNPJSpider(scrapy.Spider):
    name = "cnpj"

    def __init__(self, name=None, **kwargs):
        with open(path.join(path.abspath('.'), 'cnpj.txt'), 'r') as cnpjs:
            self.start_urls = [f'https://www.receitaws.com.br/v1/cnpj/{cnpj.strip()}' for cnpj in cnpjs]
        return super().__init__(name=name, **kwargs)


    def parse(self, response):
        # yield EmpresaItem(json.loads(response.text))
        yield json.loads(response.text)
