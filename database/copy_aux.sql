insert into store_author(id, name) select author_id, author_name from author;
insert into store_book(id, title, pub_date) select book_id, title, publication_date from book;
insert into store_book_author(book_id, author_id) select book_id, author_id from book_author;