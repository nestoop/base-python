#!/usr/bin/python
import numpy as np
print(np.zeros(5))
print(np.zeros(5, dtype=np.int))
print(np.zeros((5,5),dtype=[('x', 'i4'), ('y', 'float')]))
print(np.zeros(4, dtype=np.bool))