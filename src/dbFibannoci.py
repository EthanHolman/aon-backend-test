import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from vars import connectionString, DB_TABLE
from fibModel import Fib


def getFibRecord(num: int) -> str:
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        cursor.execute(
            f"select sequence from {DB_TABLE} where n_terms = %s;", [num])
        sequence = cursor.fetchone()

        cursor.close()
        con.close()

        return sequence
    except:
        print("Error retreiving fib record for " + num)


def putFibRecord(record: Fib):
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        cursor.execute(f"insert into {DB_TABLE} values (%s, %s, %s);",
                       (record.n_terms, record.sequence, record.time_submitted))

        cursor.close()
        con.close()
    except Exception as e:
        print("Error storing fib record for " + record.n_terms)
        print(e)
