# -*- coding: UTF-8 -*-

from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# If the inserted data has Chinese, you need to specify charset=utf8
engine = create_engine("sqlite:///database/db.sqlite3",
                       encoding='utf-8')

Base = declarative_base()  # Establish orm Base class



# After this table is created, it does not need to be maintained
store_book_author = Table("store_book_author", Base.metadata,
                        Column("id", Integer, primary_key=True),
                        Column('book_id', Integer, ForeignKey("store_book.id")),
                        Column('author_id', Integer, ForeignKey("store_author.id")))


class Book(Base):
    __tablename__ = "store_book"
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship("Author", secondary=store_book_author, backref="store_books")

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = "store_author"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


# Create table
Base.metadata.create_all(engine)
