from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

url = os.environ.get("DATABASE_URL", 'postgresql://dbuser:dbpassword@localhost:5432/dehia-mock-api')

engine = create_engine(url)
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()