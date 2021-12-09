from datetime import datetime
import calendar
import json
from fibanocci import findNFibs
from dbFibannoci import getFibRecord, putFibRecord, getQueryDatesByMonthYear


def getFibSequence(fibCount) -> str:
    record = getFibRecord(fibCount)
    if (record != None):
        return record[0]

    fobs = [str(item) for item in findNFibs(fibCount)]
    sequence = "-".join(fobs)

    now = datetime.today().strftime('%Y-%m-%d')

    putFibRecord(fibCount, sequence, now)

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

    weeklyTotals = [0] * weeksInMonth

    # yeah i know... this could be improved...
    for row in range(weeksInMonth):
        for date in dates:
            dayInMonth = int(date.strftime("%d"))
            if dayInMonth in cal[row]:
                weeklyTotals[row] += 1

    return weeklyTotals
