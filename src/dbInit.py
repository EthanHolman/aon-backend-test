import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "fib"
DB_TABLE = "fibdata"

# todo: parameterize this crap
connectionStringNoDb = "host='localhost' user='postgres' password='postgres'"
connectionString = f"{connectionStringNoDb} dbname={DB_NAME}"


def initDb():
    createDbIfNotExists()
    createSchema()


def createDbIfNotExists():
    try:
        con = psycopg2.connect(connectionStringNoDb)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        cursor.execute("select datname from pg_database;")
        result = map(list, list(cursor.fetchall()))
        result = sum(result, [])

        if (DB_NAME not in result):
            print("DB doesn't exist. Fixing that..")
            cursor.execute(f"create database {DB_NAME};")

        cursor.close()
        con.close()
    except Exception as e:
        print("Error while checking if DB exists")
        print(e)


def createSchema():
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = con.cursor()

        cursor.execute(
            f"create table {DB_TABLE} (n_terms int, sequence varchar(500), time_submitted date);")

        cursor.close()
        con.close()
    except Exception as e:
        print("Error when trying to create schema")
        print(e)
