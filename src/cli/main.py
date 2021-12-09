import sys
import requests


def showUsage():
    print("Syntax:")
    print("\t<function> <arguments>")
    print("")
    print("Functions:")
    print("calc-fib-sequence <terms-count>")
    print("\tEx: calc-fib-sequence 4")
    print("monthly-summary <month-year>")
    print("\tEx: monthly-summary 12-2021")


def runRequest(requestUrl: str):
    response = requests.get(requestUrl)
    content = response.content.decode('utf-8')
    if not content:
        print('[No Data]')
    else:
        print(content)


def calcFibSequence(termsCount: str):
    requestUrl = f"http://localhost:5000/fibonacci/{termsCount}"
    runRequest(requestUrl)


def monthlySummary(monthYear: str):
    requestUrl = f"http://localhost:5000/fibonacci/requests/{monthYear}"
    runRequest(requestUrl)


if len(sys.argv) == 3:
    fn = sys.argv[1]
    if (fn == 'calc-fib-sequence'):
        calcFibSequence(sys.argv[2])
    elif (fn == 'monthly-summary'):
        monthlySummary(sys.argv[2])
    else:
        showUsage()
else:
    showUsage()
