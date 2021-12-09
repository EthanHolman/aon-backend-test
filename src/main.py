from flask import Flask, Response
from services import getFibSequence, getRequestSummary
from dbInit import initDb
import re

# DB Initialization
initDb()

# Kick off API service

app = Flask(__name__)


@app.route("/")
def apiRoot():
    return "Fibonacci Sequence API"


@app.route("/fibonacci/<int:count>")
def apiGetFibSequence(count):
    # add input sanitization here
    return getFibSequence(count)


@app.route("/fibonacci/requests/<date>")
def apiGetRequestSummary(date):
    match = re.search("^(0?[1-9]|1[0-2])-[\d]{4}$", date)

    if match == None:
        return "Bad request. Example: /fibonacci/requests/02-2021"  # return http 4xx

    dateParts = date.split('-')
    year = int(dateParts[1])
    month = int(dateParts[0])

    summaryJson = getRequestSummary(year, month)

    return Response(summaryJson, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
