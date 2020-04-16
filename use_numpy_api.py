import numpy as np


# create arrays

np.arange(10)
np.array([1, 2, 3])
np.zeros((4, 5))
np.ones((5, 4))
np.linspace(0, 2, 100)
np.eye(10)

# attribtues
x = np.arange(10)
x.shape
x.ndim
x.dtype
x.size


# math
x + x
np.add(x, x)
np.exp(x)
np.log(x)


# comparison
x == x
x < 2

# sorting
x.sort()
x.sort(axis=0)

# slicing
x[x > 10]
x[0]
x[1:2]

# manipulation
x.T
x.reshape((5, 2))
np.column_stack([x, x])
np.concatenate((x, x), axis=0)
