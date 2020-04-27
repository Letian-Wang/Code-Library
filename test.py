# import numpy as np
# a = np.array([[1,2,3],[2,3,5]])
# print(a)
# print(a.shape)
# a = np.random.randn(2,3)
# print(a)
# print(a.shape)

# import numpy as np
# arr = np.random.randint(0,10, (3,4))
# index = np.argwhere(arr == 1)
# print(arr)
# print(index)

import numpy as np
# a = np.array([1,2,3])
# b = np.array(([2,5,8],[1,2,3]))
# C = np.array(1)
# print(C)
# list_ = []
# list_.append(a)
# list_.append(b)
# print(list_)
# c = [a,b]
# print(a)
# print(b)
# print(c)

a = np.array(1)
print(a)
a = np.array(((1,2)))
print(a)
a = np.array((1,2))
print(a)
a = np.array(((1,2),(2,3)))
print(a)
arrays = [np.random.randn(3, 4) for _ in range(10)]
print(np.stack(arrays,axis=2))
print(np.random.randn(3, 4))