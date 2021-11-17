from datetime import date
from os import path, remove

from sqlalchemy.orm import sessionmaker

from app.db import engine, init_db
from app.models import Author
from app.models import Book
from app.config import Settings


if path.exists(Settings.DATABASE_URL):
    remove(Settings.DATABASE_URL)

init_db()

# Establish session Conversation
Session_class = sessionmaker(bind=engine)
# generate session Example
session = Session_class()

b1 = Book(title="python Study", pub_date=date.fromisoformat("2018-01-01"))
b2 = Book(title="linux Study", pub_date=date.fromisoformat("2018-02-01"))
b3 = Book(title="mysql Study", pub_date=date.fromisoformat("2018-03-01"))

a1 = Author(name="Jack")
a2 = Author(name="Jerru")
a3 = Author(name="Marry")

b1.authors = [a1, a2]
b2.authors = [a2, a3]
# b3.authors = [a1, a2, a3]

session.add_all([b1, b2, a1, a2, a3])
session.commit()
