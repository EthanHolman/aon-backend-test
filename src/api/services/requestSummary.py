
import calendar
import json
from persistence.dbFibannoci import getQueryDatesByMonthYear


def getRequestSummary(year: int, month: int):
    datesInMonth = getQueryDatesByMonthYear(year, month)
    weekTotals = calcWeekTotals(year, month, datesInMonth)

    summaries = []

    for index, week in enumerate(weekTotals):
        summaries.append({"week": index + 1, "count": week})

    return json.dumps({"summary": summaries})


def calcWeekTotals(year: int, month: int, dates):
    calendar.setfirstweekday(calendar.SUNDAY)
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


def filterDatesToYearMonth(year: int, month: int, dates):
    filtered = []

    if dates != None:
        for date in dates:
            if date.strftime("%Y") == str(year) and date.strftime("%m") == str(month):
                filtered.append(date)

    return filtered
