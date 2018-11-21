# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import Column, Integer, String, Float, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    cnpj = Column(String(18), primary_key=True)
    abertura = Column(String, nullable=True)  # DATE
    atividade_principal = Column(PickleType)
    atividades_secundarias = Column(PickleType)
    bairro = Column(String)
    capital_social = Column(Float)
    cep = Column(String)
    complemento = Column(String, nullable=True)
    data_situacao = Column(String)  # DATE
    data_situacao_especial = Column(String, nullable=True)  # DATE
    efr = Column(String, nullable=True)
    email = Column(String, nullable=True)
    extra = Column(PickleType)
    fantasia = Column(String, nullable=True)
    logradouro = Column(String)
    motivo_situacao = Column(String, nullable=True)
    municipio = Column(String)
    natureza_juridica = Column(String)
    nome = Column(String, nullable=False)
    numero= Column(Integer)
    qsa = Column(PickleType)
    situacao = Column(String)
    situacao_especial = Column(String)
    status = Column(String)
    telefone = Column(String)
    tipo = Column(String)
    uf = Column(String)
    ultima_atualizacao = Column(String)  # DATE
    billing = Column(PickleType)


class StoneScrapyPipeline2DB(object):

    def __init__(self):
        engine = create_engine('sqlite:///stone_trial.db')
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        self.session = sessionmaker(bind=engine)()

    def process_item(self, item, spider):
        nova_empresa = Empresa(**item)
        self.session.add(nova_empresa)
        self.session.commit()
        return item
