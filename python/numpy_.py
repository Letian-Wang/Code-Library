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


# numpy basic
    import numpy as np
    a = np.array([[1,2,3],[4,5,6]])
    b = np.ones((1,5)) 
    c = a[0,:]

    a = np.zeros((2,2))  # Create an array of all zeros
    print a              # Prints "[[ 0.  0.]
                        #          [ 0.  0.]]"

    b = np.ones((1,2))   # Create an array of all ones
    print b              # Prints "[[ 1.  1.]]"

    c = np.full((2,2), 7) # Create a constant array
    print c               # Prints "[[ 7.  7.]
                        #          [ 7.  7.]]"

    d = np.eye(2)        # Create a 2x2 identity matrix
    print d              # Prints "[[ 1.  0.]
                        #          [ 0.  1.]]"

    e = np.random.random((2,2)) # Create an array filled with random values
    print e                     # Might print "[[ 0.91940167  0.08143941]
                                #               [ 0.68744134  0.87236687]]"

 # 整型数组访问：
    a = np.array([[1,2], [3, 4], [5, 6]])
    # An example of integer array indexing.
    # The returned array will have shape (3,) and 
    print a[[0, 1, 2], [0, 1, 0]]  # Prints "[1 4 5]"


 # 布尔型数组访问：
    a = np.array([[1,2], [3, 4], [5, 6]])

    bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                        # this returns a numpy array of Booleans of the same
                        # shape as a, where each slot of bool_idx tells
                        # whether that element of a is > 2.

    print bool_idx      # Prints "[[False False]
                        #          [ True  True]
                        #          [ True  True]]"

    # We use boolean array indexing to construct a rank 1 array
    # consisting of the elements of a corresponding to the True values
    # of bool_idx
    print a[bool_idx]  # Prints "[3 4 5 6]"

    # We can do all of the above in a single concise statement:
    print a[a > 2]     # Prints "[3 4 5 6]"

 # 数组计算
    import numpy as np

    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print x + y
    print np.add(x, y)

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print x - y
    print np.subtract(x, y)

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print x * y
    print np.multiply(x, y)

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print x / y
    print np.divide(x, y)

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print np.sqrt(x)

    # 点乘
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])

    # Inner product of vectors; both produce 219
    print v.dot(w)
    print np.dot(v, w)

    # Matrix / vector product; both produce the rank 1 array [29 67]
    print x.dot(v)
    print np.dot(x, v)

    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print x.dot(y)
    print np.dot(x, y)

    # 求和
    x = np.array([[1,2],[3,4]])
    print np.sum(x)  # Compute sum of all elements; prints "10"
    print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
    print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"

 # broadcast
    # Compute outer product of vectors
    v = np.array([1,2,3])  # v has shape (3,)
    w = np.array([4,5])    # w has shape (2,)
    # To compute an outer product, we first reshape v to be a column
    # vector of shape (3, 1); we can then broadcast it against w to yield
    # an output of shape (3, 2), which is the outer product of v and w:
    # [[ 4  5]
    #  [ 8 10]
    #  [12 15]]
    print np.reshape(v, (3, 1)) * w

    # Add a vector to each row of a matrix
    x = np.array([[1,2,3], [4,5,6]])
    # x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
    # giving the following matrix:
    # [[2 4 6]
    #  [5 7 9]]
    print x + v

    # Add a vector to each column of a matrix
    # x has shape (2, 3) and w has shape (2,).
    # If we transpose x then it has shape (3, 2) and can be broadcast
    # against w to yield a result of shape (3, 2); transposing this result
    # yields the final result of shape (2, 3) which is the matrix x with
    # the vector w added to each column. Gives the following matrix:
    # [[ 5  6  7]
    #  [ 9 10 11]]
    print (x.T + w).T

    # Another solution is to reshape w to be a row vector of shape (2, 1);
    # we can then broadcast it directly against x to produce the same
    # output.
    print x + np.reshape(w, (2, 1))

    # Multiply a matrix by a constant:
    # x has shape (2, 3). Numpy treats scalars as arrays of shape ();
    # these can be broadcast together to shape (2, 3), producing the
    # following array:
    # [[ 2  4  6]
    #  [ 8 10 12]]
    print x * 2