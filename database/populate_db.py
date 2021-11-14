from database.m2m_orm import engine


def populate_db():
    list_scripts = (
        "database/create_aux_schema.sql",
        "database/source_data/02_populate_author.sql",
        "database/source_data/03_populate_publisher.sql",
        "database/source_data/04_populate_language.sql",
        "database/source_data/05_populate_book.sql",
        "database/source_data/06_populate_bookauthor.sql",
        "database/copy_aux.sql",
    )

    separator = ';'
    for script in list_scripts:
        with open(script) as f:
            schema = f.read()
            with engine.connect() as con:
                if script in (list_scripts[0], list_scripts[-1]):
                    for schema_statement in schema.split(separator):
                        con.execute(schema_statement + separator)
                else:
                    con.execute(schema)
