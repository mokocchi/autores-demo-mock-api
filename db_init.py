from entities.dominio import Dominio
from base import session_factory, engine, Base
import os

def db_init():
    Base.metadata.create_all(engine)
    session = session_factory()

    dominios = []
    dominios.append(Dominio("Pruebas"))
    for dominio in dominios:
        session.add(dominio)

    session.commit()
    session.close()