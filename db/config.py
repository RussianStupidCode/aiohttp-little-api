import os

SALT = 'my_sJHLHLHKLаваыпuper_s!alt_#4$4344'

DATABASE = {
    'drivername': os.getenv("DB_DRIVERNAME", 'postgresql'),
    'host': os.getenv("DB_HOST", 'db'),
    'port': os.getenv("DB_PORT", '5432'),
    'username': os.getenv("POSTGRES_USER"),
    'password': os.getenv("POSTGRES_PASSWORD"),
    'database': os.getenv("POSTGRES_DB")
}