from database.m2m_orm import engine
from database.m2m_orm import Author
from database.m2m_orm import Book
from sqlalchemy.orm import sessionmaker

# Establish session Conversation
Session_class = sessionmaker(bind=engine)
# generate session Example
session = Session_class()

print("Check related books through the author table".center(30, '-'))
author_obj = session.query(Author).filter(Author.name=='Jack').first()
print(author_obj.name, author_obj.books, author_obj.books[0].pub_date)

print("Check related authors through book list".center(30, '-'))
book_obj = session.query(Book).filter(Book.id==2).first()
print(book_obj.name, book_obj.authors)