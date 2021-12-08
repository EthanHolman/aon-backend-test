from datetime import datetime
from fibanocci import findNFibs
from dbFibannoci import getFibRecord, putFibRecord
from fibModel import Fib


def getFibSequence(fibCount) -> str:
    record = getFibRecord(fibCount)
    if (record != None):
        return record[0]

    fobs = [str(item) for item in findNFibs(fibCount)]
    sequence = "-".join(fobs)

    now = datetime.today().strftime('%Y-%m-%d')

    fib = Fib(fibCount, sequence, now) #convert to tuple?
    putFibRecord(fib)

    return sequence
