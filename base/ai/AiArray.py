import numpy as np
from scipy import sparse

a = np.array([[1, 2, 4], [5, 7, 8]])

print("a:\n {}".format(a))

eye = np.eye(4)

print("Numpy Array:\n {}".format(eye))

# use matrix
sparse_matrix = sparse.csr_matrix(eye)

print("Scipy sparse csr Array:\n {}".format(sparse_matrix))

#
data = np.ones(4)
row_indexs = np.arange(4)
clo_indexs = np.arange(4)
print("data:\n {}".format(data))
print("row_indexs:\n {}".format(row_indexs))
print("clo_indexs:\n {}".format(clo_indexs))
eye_coo = sparse.coo_matrix(data, (row_indexs, clo_indexs))
print("Scipy sparse coo Array:\n {}".format(eye_coo))





