# save
from scipy.io import savemat
import numpy as np
a = np.arange(20)
mdic = {"a": a, "label": "experiment"}
# mdic
# {'a': array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#     17, 18, 19]),
# 'label': 'experiment'}
savemat("matlab_matrix.mat", mdic)

# read
import scipy.io
mat = scipy.io.loadmat('file.mat')