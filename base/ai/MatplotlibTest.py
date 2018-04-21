#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# create a array
x = np.arange(0, 5, 0.1)
y = np.sin(x)

example = plt.plot(x, y)
example = plt.title("x: array Y sin method")
example = plt.xlabel("X")
example = plt.ylabel("Sin")
example.figure.savefig("example", bbox_inches='tight')



