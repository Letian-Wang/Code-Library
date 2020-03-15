import numpy as np
import matplotlib as plt
# Numpy
a = np.array([[1,2,3],[4,5,6]])
b = np.ones((2,4))
b = np.zeros((2,4))
d = np.zeros_like(b)
c = b[0,0]
b[0:1,0]                            # length is 1 rather than 2
len(b)

# Dictionary
traj = data[1]                      # data include many dictionaries
plt.scatter(traj['egowholeTraj'][0],traj['egowholeTraj'][1], s=8, marker=".", color = 'red') # s means size
plt.show()

for name,dict_ in data[1].items():
    print( 'the name of the dictionary is ', name)
    print( 'the dictionary looks like ', dict_)

# List
record = [[0 for i in range(3)] for j in range(2)]      # Create a list with (2,3)
record[0].index(min(record[0]))                         # Find the minmum value and the corresponding index
