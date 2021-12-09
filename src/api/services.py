from datetime import datetime
import calendar
import json
from dbFibannoci import putFibRecord, getQueryDatesByMonthYear


def getFibSequence(fibCount: int) -> str:
    sequence = ""

    if fibCount > 0:
        fobs = [str(item) for item in findNFibs(fibCount)]
        sequence = "-".join(fobs)

        now = datetime.today().strftime('%Y-%m-%d')

        putFibRecord(str(fibCount), sequence, now)

    return sequence


def getRequestSummary(year: int, month: int):
    datesInMonth = getQueryDatesByMonthYear(year, month)
    weekTotals = calcWeekTotals(year, month, datesInMonth)

    summaries = []

    for index, week in enumerate(weekTotals):
        summaries.append({"week": index + 1, "count": week})

    return json.dumps({"summary": summaries})


def calcWeekTotals(year: int, month: int, dates):
    cal = calendar.monthcalendar(year, month)
    weeksInMonth = len(cal)

    dates = filterDatesToYearMonth(year, month, dates)

    weeklyTotals = [0] * weeksInMonth

    for row in range(weeksInMonth):
        for date in dates:
            dayInMonth = int(date.strftime("%d"))
            if dayInMonth in cal[row]:
                weeklyTotals[row] += 1

    return weeklyTotals


def findNFibs(fibCount):
    result = []

    if fibCount > 0:
        a, b = 0, 1

        while len(result) < fibCount:
            result.append(a)
            a, b = b, a + b

    return result


def filterDatesToYearMonth(year: int, month: int, dates):
    filtered = []

    for date in dates:
        if date.strftime("%Y") == str(year) and date.strftime("%m") == str(month):
            filtered.append(date)

    return filtered
