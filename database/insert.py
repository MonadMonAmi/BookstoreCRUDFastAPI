# -*- coding: UTF-8 -*-
from datetime import date

from database.m2m_orm import engine
from database.m2m_orm import Author
from database.m2m_orm import Book
from sqlalchemy.orm import sessionmaker

# Establish session Conversation
Session_class = sessionmaker(bind=engine)
# generate session Example
session = Session_class()

b1 = Book(name="python Study", pub_date=date.fromisoformat("2018-01-01"))
b2 = Book(name="linux Study", pub_date=date.fromisoformat("2018-02-01"))
b3 = Book(name="mysql Study", pub_date=date.fromisoformat("2018-03-01"))

a1 = Author(name="Jack")
a2 = Author(name="Jerru")
a3 = Author(name="Marry")

b1.authors = [a1,a2]
b2.authors = [a2,a3]
b3.authors = [a1,a2,a3]

session.add_all([b1,b2,b3,a1,a2,a3])
session.commit()