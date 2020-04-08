# coding=utf-8

from sqlalchemy import Column, String, Integer

from base import Base


class TipoTarea(Base):
    __tablename__ = 'tipo_tarea'
    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String(32))
    codigo = Column('codigo', String(32))

    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo": self.codigo
        }
