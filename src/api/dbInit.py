import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from vars import DB_NAME, DB_TABLE, connectionStringNoDb, connectionString


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
        print("[Error] while checking if DB exists. Exiting..")
        print(e)
        sys.exit(1)


def createSchema():
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = con.cursor()

        cursor.execute(
            f"create table if not exists {DB_TABLE} (n_terms int primary key, sequence varchar(10000) not null, time_submitted date not null);")

        cursor.close()
        con.close()
    except Exception as e:
        print("[Error] when trying to create schema. Exiting..")
        print(e)
        sys.exit(1)
