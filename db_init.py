from entities.dominio import Dominio
from entities.estado import Estado
from entities.tipo_tarea import TipoTarea
from entities.actividad import Actividad
from base import session_factory, engine, Base
import os


def db_init():
    Base.metadata.create_all(engine)
    session = session_factory()

    actividad = Actividad()
    session.add(Actividad)

    dominios = []
    dominios.append(Dominio("Pruebas"))
    for dominio in dominios:
        session.add(dominio)

    estados = []
    estados.append(Estado("Público"))
    estados.append(Estado("Privado"))
    for estado in estados:
        session.add(estado)

    tipos_tarea = []
    tipos_tarea.append(TipoTarea("Simple", "simple"))
    tipos_tarea.append(TipoTarea("Ingresar texto", "textInput"))
    tipos_tarea.append(TipoTarea("Ingresar un número", "numberInput"))
    tipos_tarea.append(TipoTarea("Sacar foto", "cameraInput"))
    tipos_tarea.append(TipoTarea("Elegir una opción", "select"))
    tipos_tarea.append(TipoTarea("Opción múltiple", "multiple"))
    tipos_tarea.append(TipoTarea("Contadores", "counters"))
    tipos_tarea.append(TipoTarea("Recolección", "collect"))
    tipos_tarea.append(TipoTarea("Depósito", "deposit"))
    tipos_tarea.append(TipoTarea("Localización", "GPSInput"))
    tipos_tarea.append(TipoTarea("Grabar audio", "audioInput"))
    for tipo_tarea in tipos_tarea:
        session.add(tipo_tarea)

    session.commit()
    session.close()
