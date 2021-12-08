import os

DB_NAME = "fib"
DB_TABLE = "fibdata"
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

connectionStringNoDb = f"host={DB_HOST} user={DB_USER} password={DB_PASS}"
connectionString = f"{connectionStringNoDb} dbname={DB_NAME}"
