from os import environ


class Settings:
    DATABASE_URL = environ.get("DATABASE_URL")
