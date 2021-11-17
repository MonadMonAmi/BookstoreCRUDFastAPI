from app.db import init_db
from database.populate_db import populate_db


if __name__ == '__main__':
    init_db()
    populate_db()
