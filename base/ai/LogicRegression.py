import numpy as np


def aig(x):
    '''
    sigmoid function
    :param x:
    :return:
    '''
    return 1.0 / (1 + np.exp(-x))
