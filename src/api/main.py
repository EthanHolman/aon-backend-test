import re
from flask import Flask, Response
from services import getFibSequence, getRequestSummary
from dbInit import initDb

# app startup
initDb()
api = Flask(__name__)


@api.route("/")
def apiRoot():
    return Response("Fibonacci Sequence API", mimetype='text/plain')


@api.route("/fibonacci/<count>")
def apiGetFibSequence(count):
    match = re.search("^[\d]+$", count)

    if match == None:
        return Response("Bad request. Example: /fibonacci/12", status=400)

    sequence = getFibSequence(count)
    return Response(sequence, mimetype='text/plain')


@api.route("/fibonacci/requests/<date>")
def apiGetRequestSummary(date):
    match = re.search("^(0?[1-9]|1[0-2])-[\d]{4}$", date)

    if match == None:
        return Response("Bad request. Example: /fibonacci/requests/02-2021", status=400)

    dateParts = date.split('-')
    year = int(dateParts[1])
    month = int(dateParts[0])

    summaryJson = getRequestSummary(year, month)
    return Response(summaryJson, mimetype='application/json')


if __name__ == '__main__':
    api.run(host="0.0.0.0")
