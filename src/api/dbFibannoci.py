import datetime
import calendar
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from vars import connectionString, DB_TABLE


def putFibRecord(n_terms, sequence, time_submitted):
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        cursor.execute(f"insert into {DB_TABLE} values (%s, %s, %s);",
                       (n_terms, sequence, time_submitted))

        cursor.close()
        con.close()
    except Exception as e:
        print("Error storing fib record for " + n_terms)
        print(e)


def getQueryDatesByMonthYear(year: int, month: int):
    try:
        con = psycopg2.connect(connectionString)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        daysInMonth = calendar.monthrange(year, month)[1]

        startDate = datetime.datetime(year, month, 1)
        endDate = datetime.datetime(year, month, daysInMonth)

        cursor.execute(
            f"select time_submitted from {DB_TABLE} where time_submitted >= %s and time_submitted  <= %s order by time_submitted asc;", (startDate, endDate))

        tuplesToFlatten = cursor.fetchall()

        cursor.close()
        con.close()

        return list(sum(tuplesToFlatten, ()))
    except Exception as e:
        print("Error getting dates by month/year")
        print(e)
