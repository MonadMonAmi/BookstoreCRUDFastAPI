from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()  # Establish orm Base class

# After this table is created, it does not need to be maintained
store_book_author = Table(
    "store_book_author", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column('book_id', Integer, ForeignKey("store_book.id")),
    Column('author_id', Integer, ForeignKey("store_author.id"))
)

'''
class store_book_author(Base):
    __tablename__ = "store_book_author"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("store_book.id"))
    author_id = Column(Integer, ForeignKey("store_author.id"))
    
class Table(DialectKWArgs, SchemaItem, TableClause):
    r"""Represent a table in a database.

    e.g.::

        mytable = Table("mytable", metadata,
                        Column('mytable_id', Integer, primary_key=True),
                        Column('value', String(50))
                   )

    The :class:`_schema.Table`
    object constructs a unique instance of itself based
    on its name and optional schema name within the given
    :class:`_schema.MetaData` object. Calling the :class:`_schema.Table`
    constructor with the same name and same :class:`_schema.MetaData` argument
    a second time will return the *same* :class:`_schema.Table`
    object - in this way
    the :class:`_schema.Table` constructor acts as a registry function.

    .. seealso::

        :ref:`metadata_describing` - Introduction to database metadata
        

def def declarative_base() ...
    r"""Construct a base class for declarative class definitions.

    The new base class will be given a metaclass that produces
    appropriate :class:`~sqlalchemy.schema.Table` objects and makes
    the appropriate :func:`~sqlalchemy.orm.mapper` calls based on the
    information provided declaratively in the class and any subclasses
    of the class.

    The :func:`_orm.declarative_base` function is a shorthand version
    of using the :meth:`_orm.registry.generate_base`
    method.  That is, the following::

        from sqlalchemy.orm import declarative_base

        Base = declarative_base()

    Is equivalent to::

        from sqlalchemy.orm import registry

        mapper_registry = registry()
        Base = mapper_registry.generate_base()

    See the docstring for :class:`_orm.registry`
    and :meth:`_orm.registry.generate_base`
    for more details.

    .. versionchanged:: 1.4  The :func:`_orm.declarative_base`
       function is now a specialization of the more generic
       :class:`_orm.registry` class.  The function also moves to the
       ``sqlalchemy.orm`` package from the ``declarative.ext`` package.
'''


class Book(Base):
    __tablename__ = "store_book"
    id = Column(Integer, primary_key=True)
    title = Column(String(400))
    pub_date = Column(DATE)
    authors = relationship("Author", secondary=store_book_author, backref="store_books")
    unique_constraint = UniqueConstraint('title', 'pub_date')

    def __repr__(self):
        return self.title


class Author(Base):
    __tablename__ = "store_author"
    id = Column(Integer, primary_key=True)
    name = Column(String(400))#, unique=True)

    def __repr__(self):
        return self.name
