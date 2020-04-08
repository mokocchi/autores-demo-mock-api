# coding=utf-8

from sqlalchemy import Column, String, Integer

from base import Base


class Estado(Base):
    __tablename__ = 'estado'
    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String(32))

    def __init__(self, nombre):
        self.nombre = nombre

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }
