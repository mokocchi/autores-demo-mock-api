# coding=utf-8

from sqlalchemy import Column, String, Integer

from base import Base

class Dominio(Base):
    __tablename__ = 'dominio'
    id=Column(Integer, primary_key=True)
    nombre=Column('nombre', String(32))

    def __init__(self, nombre):
        self.nombre = nombre