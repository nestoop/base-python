# coding=utf-8
"""
归纳证明算法
"""


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([1, 10, 20, 4, 6, 0, 4, 8, 9,45, 3]))
