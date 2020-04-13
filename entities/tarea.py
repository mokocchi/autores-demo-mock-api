# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, ForeignKey, JSON

from base import Base


class Tarea(Base):
    __tablename__ = 'tarea'
    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String(32))
    consigna = Column('consigna', String(255))
    extra = Column('extra', JSON)
    codigo = Column('codigo', String(255))
    dominio_id = Column(Integer, ForeignKey('dominio.id'))
    estado_id = Column(Integer, ForeignKey('estado.id'))
    tipo_tarea_id = Column(Integer, ForeignKey('tipo_tarea.id'))

    def __init__(self, nombre, consigna, extra, codigo, dominio, estado, tipo_tarea):
        self.nombre = nombre
        self.consigna = consigna
        self.extra = extra
        self.codigo = codigo
        self.dominio = dominio
        self.estado = estado
        self.tipo_tarea = tipo_tarea
        self.dominio_id = dominio.id
        self.estado_id = estado.id
        self.tipo_tarea_id = tipo_tarea.id

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "consigna": self.consigna,
            "dominio": self.dominio.to_json(),
            "estado": self.estado.to_json(),
            "tipo_tarea": self.tipo_tarea.to_json()
        }
    
    def set_dominio(self, dominio):
        self.dominio = dominio
    
    def set_estado(self, estado):
        self.estado = estado
    
    def set_tipo_tarea(self, tipo_tarea):
        self.tipo_tarea = tipo_tarea
