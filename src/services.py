from fibanocci import findNFibs

def getFibSequence(fibCount):
    fobs = [str(item) for item in findNFibs(fibCount)]
    sequence = "-".join(fobs)
    return sequence

