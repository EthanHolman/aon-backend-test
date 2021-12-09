def findNFibs(fibCount):
    result = []
    a, b = 0, 1

    while len(result) < fibCount:
        result.append(a)
        a, b = b, a + b

    return result
