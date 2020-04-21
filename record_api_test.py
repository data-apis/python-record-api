import operator as op
import sys
import unittest
from unittest.mock import call, patch

import numpy as np

from record_api import Tracer


class TestMockNumPyMethod(unittest.TestCase):
    def setUp(self):
        self.a = np.arange(10)
        patcher = patch("record_api.log_call")
        self.mock = patcher.start()
        self.addCleanup(patcher.stop)
        self.tracer = Tracer("numpy")

    def test_pos(self):
        with self.tracer:
            +self.a
        self.mock.assert_called_once_with(op.pos, self.a)

    def test_neg(self):
        with self.tracer:
            -self.a
        self.mock.assert_called_once_with(op.neg, self.a)

    def test_invert(self):
        with self.tracer:
            ~self.a
        self.mock.assert_called_once_with(op.invert, self.a)

    def test_add(self):
        with self.tracer:
            self.a + 10
        self.mock.assert_called_once_with(op.add, self.a, 10)

    def test_radd(self):
        with self.tracer:
            # verify regulaar add doesnt add
            10 + 10
            10 + self.a
        self.mock.assert_called_once_with(op.add, 10, self.a)

    def test_iadd(self):
        with self.tracer:
            self.a += 10
        self.mock.assert_called_once_with(op.iadd, self.a, 10)

    def test_getitem(self):
        l = [self.a]
        with self.tracer:
            self.a[0]
            # verify is value in np array doesn't count
            l[0]
        self.mock.assert_called_once_with(op.getitem, self.a, 0)

    def test_setitem(self):
        l = [0]
        with self.tracer:
            self.a[0] = 1
            # verify is value in np array doesn't count
            l[0] = self.a
        self.mock.assert_called_once_with(op.setitem, self.a, 0, 1)

    def test_setattr(self):
        with self.tracer:
            self.a.shape = (10, 1)
            # verify attr doesnt match
            o = lambda: None
            o.something = self.a
        self.mock.assert_called_once_with(setattr, self.a, "shape", (10, 1))

    def test_tuple_unpack(self):
        with self.tracer:
            (*self.a, 10, *self.a)
        iter_ = call(iter, self.a)
        assert self.mock.mock_calls == [iter_, iter_]

    def test_tuple_unpack_with_call(self):
        def f(*args):
            pass

        with self.tracer:
            f(*self.a, 10, *self.a)
        iter_ = call(iter, self.a)
        assert self.mock.mock_calls == [iter_, iter_]

    def test_load_attr(self):
        o = lambda: None
        o.shape = (1,)
        with self.tracer:
            self.a.shape
            # verify normal object doesn't trigger
            o.shape
        self.mock.assert_called_once_with(getattr, self.a, "shape")


if __name__ == "__main__":
    unittest.main()
