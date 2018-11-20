import scrapy
import json
from os import path

class CNPJSpider(scrapy.Spider):
    name = "cnpj"

    def __init__(self, name=None, **kwargs):
        with open(path.join(path.abspath('.'), 'cnpj.txt'), 'r') as cnpjs:
            self.start_urls = [f'https://www.receitaws.com.br/v1/cnpj/{cnpj.strip()}' for cnpj in cnpjs]
        return super().__init__(name=name, **kwargs)


    def parse(self, response):
        yield json.loads(response.text)