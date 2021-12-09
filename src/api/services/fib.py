from datetime import datetime
from persistence.dbFibannoci import putFibRecord


def getFibSequence(fibCount: int) -> str:
    sequence = ""

    if fibCount > 0:
        fobs = [str(item) for item in findNFibs(fibCount)]
        sequence = "-".join(fobs)

        now = datetime.today().strftime('%Y-%m-%d')

        putFibRecord(str(fibCount), sequence, now)

    return sequence


def findNFibs(fibCount):
    result = []

    if fibCount > 0:
        a, b = 0, 1

        while len(result) < fibCount:
            result.append(a)
            a, b = b, a + b

    return result
