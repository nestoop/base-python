# coding=utf-8
"""
K-近邻算法
"""

from numpy import *
import operator


def createDataSet():
    groups = array([[1, 1.1], [2, 3.1], [9, 5.1],  [6, 7.1]])
    labels = ['A', 'B', "A", "B"]
    return groups, labels


groups, labels = createDataSet()
print(groups)
print(labels)
