import os

from sqlalchemy import create_engine

from app.models import Base
from app.config import Settings


engine = create_engine(
    Settings.DATABASE_URL,
    encoding='utf-8'
)


def init_db():
    Base.metadata.create_all(engine)
