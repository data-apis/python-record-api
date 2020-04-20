import unittest
import os
import sys
from unittest.mock import call, patch
import numpy as np

os.environ["PYTHON_API_TRACE_MODULE"] = "numpy"
# defer import so environ can be set first
from record_api import tracer


class TestMockNumPyMethod(unittest.TestCase):
    def setUp(self):
        self.a = np.arange(10)
        patcher = patch("record_api.log_call")
        self.mock = patcher.start()
        self.addCleanup(patcher.stop)

        sys.settrace(tracer)
        self.addCleanup(sys.settrace, None)

    def test_pos(self):
        +self.a
        self.mock.assert_called_once_with(np.ndarray.__pos__, "numpy", self.a)

    def test_neg(self):
        -self.a
        self.mock.assert_called_once_with(np.ndarray.__neg__, "numpy", self.a)

    def test_invert(self):
        ~self.a
        self.mock.assert_called_once_with(np.ndarray.__invert__, "numpy", self.a)

    def test_add(self):
        self.a + 10
        self.mock.assert_called_once_with(np.ndarray.__add__, "numpy", self.a, 10)

    def test_radd(self):
        10 + self.a
        self.mock.assert_called_once_with(np.ndarray.__radd__, "numpy", self.a, 10)

    def test_iadd(self):
        self.a += 10
        self.mock.assert_called_once_with(np.ndarray.__iadd__, "numpy", self.a, 10)

    def test_setitem(self):
        self.a[0] = 1
        self.mock.assert_called_once_with(np.ndarray.__setitem__, "numpy", self.a, 0, 1)

    def test_setattr(self):
        self.a.shape = (10, 1)
        self.mock.assert_called_once_with(
            np.ndarray.__setattr__, "numpy", self.a, "shape", (10, 1)
        )

    def test_tuple_unpack(self):
        t = (*self.a, 10, *self.a)
        iter_ = call(np.ndarray.__iter__, "numpy", self.a)
        assert self.mock.mock_calls == [iter_, iter_]

    def test_tuple_unpack_with_call(self):
        def f(*args):
            pass

        f(*self.a, 10, *self.a)
        iter_ = call(np.ndarray.__iter__, "numpy", self.a)
        assert self.mock.mock_calls == [iter_, iter_]

    def test_load_attr(self):
        self.a.shape
        self.mock.assert_called_once_with(
            np.ndarray.__getattr__, "numpy", self.a, "shape"
        )


if __name__ == "__main__":
    unittest.main()
