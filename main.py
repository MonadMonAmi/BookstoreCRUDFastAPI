from database.m2m_orm import create_tables
from database.populate_db import populate_db

if __name__ == '__main__':
    create_tables()
    populate_db()
