# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, ForeignKey, JSON
from sqlalchemy.orm import relationship

from base import Base
from entities.tarea import Tarea


class Actividad(Base):
    __tablename__ = 'actividad'
    id = Column(Integer, primary_key=True)
    tareas = relationship("Tarea", order_by=Tarea.id,
                          back_populates="actividad")

    def __init__(self):
        self.tareas = []

    def get_tareas(self):
        return self.tareas
