from flask import Flask
from services import getFibSequence
from dbInit import initDb

# DB Initialization
initDb()

# Kick off API service

app = Flask(__name__)

@app.route("/")
def apiRoot():
    return "Fibonacci Sequence API"

@app.route("/fibonacci/<int:count>")
def apiGetFibSequence(count):
    return getFibSequence(count)

@app.route("/fibonacci/requests/<date>")
def apiGetRequestSummary(date):
    return "This part is unclear: " + date

if __name__ == '__main__':
    app.run(host="0.0.0.0" )
