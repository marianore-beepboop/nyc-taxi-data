from decouple import AutoConfig

from project.constants import REPO_ROOT

config = AutoConfig(search_path=REPO_ROOT)

PG_CFG = {
    "dialect": config("POSTGRES_DIALECT", default="postgres", cast=str),
    "driver": config("POSTGRES_DRIVER", default="psycopg2", cast=str),
    "username": config("POSTGRES_USER", default="root", cast=str),
    "password": config("POSTGRES_PASSWORD", default="root", cast=str),
    "host": config("POSTGRES_HOST", default="localhost", cast=str),
    "port": config("POSTGRES_INTERNAL_PORT", default=5432, cast=int),
    "database": config("POSTGRES_DB", default="nyc_taxi_db", cast=str),
}
