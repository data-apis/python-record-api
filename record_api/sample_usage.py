import numpy as np


def fn():
    x = np.arange(10)
    # unary method
    +x
    -x
    ~x

    # bool or length
    try:
        not x
    except ValueError:
        pass
    # iter
    for _ in x:
        pass

    # binary methods
    x[0]
    y = 2

    x ** y
    y ** x
    x * y
    y * x
    x @ x
    x // y
    y // x
    x % y
    y % x
    x + y
    y + x
    x - y
    y - x
    x << y
    y << x
    x >> y
    y >> x
    x & y
    y & x
    x | y
    y | x

    y = 2
    x **= y
    y = 2
    y **= x
    y = 2
    x *= y
    y = 2
    y *= x
    y = 2
    x //= y
    x %= y
    x += y
    x -= y
    x <<= y
    x >>= y
    x &= y
    x |= y
    x[0] = y

    np.array("df")
    # Long string should be recorded properly
    np.array("df" * 100)

    # unpack
    _, *_s = x

    # create arrays
    np.dtype(np.int16)

    np.random.mtrand.RandomState(0).random()
    np.arange(10)
    np.array([1, 2, 3])
    np.zeros((4, 5))
    np.ones((5, 4))
    np.linspace(0, 2, 100)
    np.eye(10)

    # attribtues
    x = np.arange(10)
    x.shape
    x.shape = (10, 1)
    x.ndim
    x.dtype
    x.size

    # math

    x + x
    np.add(x, x)
    np.exp(x)
    np.log(x)
    x.mean()
    # as class method
    np.ndarray.mean(x)

    # actual class method
    np.polynomial.chebyshev.Chebyshev.basis(10)

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
    np.arange(10).reshape(5, 2)[((1, 2, 3), (0, 1, 1))]

    # manipulation
    x.T
    x.reshape((5, 2))
    np.column_stack([x, x])
    np.concatenate((x, x), axis=0)
    x.astype(int)

    # contains
    1 in x

    # reduction
    np.add.reduce(x)

    np.ndarray((0, 1, 2))


fn()
