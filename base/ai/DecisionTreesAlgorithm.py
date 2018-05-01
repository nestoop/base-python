#!/usr/bin/python
from math import log
"""
香农熵算法

1.every one of variable x Shanno = log2p(x)
"""
def calcShannoEnt(dataSet):
    dataSetSize = len(dataSet)
    lableCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in lableCounts.keys():
            lableCounts[currentLabel] = 0
        lableCounts[currentLabel] += 1

    shannoEnt = 0.0
    for key in lableCounts:
        prod = float(lableCounts[key] / dataSetSize)
        shannoEnt -= prod * log(prod, 2)
    return shannoEnt


