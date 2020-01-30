# plot scatter
import matplotlib.pyplot as plt 
plt.scatter(data[:,:,0], data[:,:,1], s=8, marker=".", color = 'red') # s means size
plt.show()

# 3d plot scatter
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D ## 3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0,0], data[:,0,1], data[:,0], s=2, marker=".")
plt.show()

# numpy basic
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.ones((1,5)) 
c = a[0,:]

# load data .mat
import scipy.io as sio
file = 'data.mat'
data = sio.loadmat(file)