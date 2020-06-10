import numpy as np
from mpl_toolkits.mplot3d import axes3d

# value
a = np.array(((1,2,3),(4,5,6)))
a = np.array((1,2,3))               # equals below
a = np.array((1,2,3))               # equals above
b = np.ones((2,4))
b = np.zeros((2,4))
d = np.zeros_like(b)
c = b[0,0]
b[0:1,0]                            # length is 1 rather than 2
len(b)

#operation
a.shape
a.transpose()
a = np.ravel(a, order = 'C')                    # C：row order(c style)     F: column order(fortran style) 
                                                # A: read the element in its style(C/F)   K: read the element in its memory order 
a.flat                                          # flat into one dimension 
b= np.flatten(a)                                # return a one-dimension copy in row major order 
b = a.reshape(2,-1)                             # -1 means only col number need to be adapted
a = b.view()                                    # copy another variable without changing the original one

np.split(x,3,axis=0)                            # split x into 3 arrays
np.dsplit()
np.vsplit()
np.hsplit()

np.vstack((a,b))                                # Stack arrays in sequence vertically (row wise)
np.hstack((a,b))                                # Stack arrays in sequence horizontally (column wise)
np.stack((a,b),axis = 0)                        # Join a sequence of arrays along a new axis. 
                                                # add new axis in the same position of parameter axis
                                                # if axis=0 it will be the first dimension and if axis=-1 it will be the last dimension.
np.dstack                                       # for array less than 3 dimension, stack arrays in sequence depth wise (along third axis)

np.concatenate((a, b), axis=0)                  # Join a sequence of arrays along an existing axis.  (axix=0 is vertically, axis = 1 is horizontally)    
np.block([A, B])                                # Horizontally Assemble an nd-array from nested lists of blocks 
np.block([[A], [B]])                            # Verticaelly Assemble an nd-array from nested lists of blocks

# creation
x = np.linspace(2,3,5)                  # number
y = np.arange(-3.0, 3.0, 1)             # step
X, Y, Z = axes3d.get_test_data(0.1)     # bivariate normal distribution
X, Y = np.meshgrid(x, y)
grid = np.indices((2,3))

# calculation
from matplotlib.mlab import bivariate_normal
bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0, mux=0.0, muy=0.0, sigmaxy=0.0)

# random
import random
r3 = random.randint(-5, 5) 
arr0 = np.random.randint(1,5, size=(2, 4))      # random integer between 1(inclusive) and 5(exclusive), with shape of size 
arr1 = np.random.randn(2,4)                     # standard normal distribution
arr2 = np.random.rand(2,4)                      # random number between 0 and 1

# index
arr = np.random.randint(0,10, (3,4))
index = np.argwhere(arr < 5)

# numpy format conversion
    a.dtype                                  # check format
    a = np.array(a).astype('float')          # convert formatarr2.dtype

# expand dimension: (10000, 28, 28) -> (10000, 28, 28, 1))
    a = np.expand_dims(a, axis=3)