import operator as op
import sys
import unittest
from unittest.mock import call, patch, ANY

import numpy as np
import pandas as pd

from . import Tracer


class BaseTest(unittest.TestCase):
    def setUp(self):
        patcher = patch("record_api.core.log_call")
        self.mock = patcher.start()
        self.addCleanup(patcher.stop)

    def trace(self, source: str):
        """
        use exec so that it is called in child scope.

        alternatively could use IIFE but this is more verbose
        in the tests
        """
        with self.tracer:  # type: ignore
            exec(source)

    def assertCalls(self, *calls):
        self.assertListEqual(
            self.mock.mock_calls, [*calls],
        )


class TestMockNumPyMethod(BaseTest):
    def setUp(self):
        super().setUp()
        self.a = np.arange(10)
        self.tracer = Tracer(["numpy"], ["record_api.test"])

    def test_pos(self):
        self.trace("+self.a")
        self.mock.assert_called_once_with(ANY, op.pos, self.a)

    def test_neg(self):
        self.trace("-self.a")
        self.mock.assert_called_once_with(ANY, op.neg, self.a)

    def test_invert(self):
        self.trace("~self.a")
        self.mock.assert_called_once_with(ANY, op.invert, self.a)

    def test_add(self):
        self.trace("self.a + 10")
        self.mock.assert_called_once_with(ANY, op.add, self.a, 10)

    def test_radd(self):
        # verify regular add doesn't add
        self.trace("10 + 10")
        self.trace("10 + self.a")
        self.mock.assert_called_once_with(ANY, op.add, 10, self.a)

    def test_iadd(self):
        self.trace("self.a += 10")
        self.mock.assert_called_once_with(ANY, op.iadd, self.a, 10)

    def test_getitem(self):
        # verify regular getitem doesnt trigger
        self.trace("[self.a][0]")
        self.trace("self.a[0]")
        self.mock.assert_called_once_with(ANY, op.getitem, self.a, 0)

    def test_setitem(self):
        # verify regular setitem doesnt trigger
        self.trace("l = [0]\nl[0] = self.a")
        self.trace("self.a[0] = 1")
        self.mock.assert_called_once_with(ANY, op.setitem, self.a, 0, 1)

    def test_setattr(self):
        self.trace("self.a.shape = (10, 1)")
        # Verify normal setattr doesn't trigger
        self.trace("o = lambda: None\no.something = self.a")
        self.mock.assert_called_once_with(ANY, setattr, self.a, "shape", (10, 1))

    def test_tuple_unpack(self):
        self.trace("(*self.a, 10, *self.a)")
        iter_ = call(ANY, iter, self.a)
        self.assertCalls(iter_, iter_)

    def test_tuple_unpack_with_call(self):
        self.trace("def f(*args): pass\nf(*self.a, 10, *self.a)")
        iter_ = call(ANY, iter, self.a)
        self.assertCalls(iter_, iter_)

    def test_load_attr(self):
        # verify normal object doesn't trigger
        self.trace("o = lambda: None\no.shape = self.a\no.shape")
        self.trace("self.a.shape")
        self.mock.assert_called_once_with(ANY, getattr, self.a, "shape")

    def test_arange(self):
        self.trace("np.arange(10)")
        self.mock.assert_called_once_with(ANY, np.arange, 10)

    def test_arange_in_fn(self):
        self.trace("(lambda: np.arange(10))()")
        self.mock.assert_called_once_with(ANY, np.arange, 10)

    def test_power(self):
        self.trace("np.power(100, 10)")
        self.mock.assert_called_once_with(ANY, np.power, 100, 10)

    def test_sort(self):
        self.trace("self.a.sort(axis=0)")
        self.assertCalls(
            call(ANY, getattr, self.a, "sort"), call(ANY, self.a.sort, axis=0),
        )

    def test_eye(self):
        self.trace("np.eye(10, order='F')")
        self.assertCalls(
            call(ANY, getattr, np, "eye"), call(ANY, np.eye, 10, order="F"),
        )

    def test_linspace(self):
        self.trace("np.linspace(3, 4, endpoint=False)")
        self.assertCalls(
            call(ANY, getattr, np, "linspace"),
            call(ANY, np.linspace, 3, 4, endpoint=False),
        )

    def test_reshape(self):
        self.trace("self.a.reshape((5, 2))")
        self.assertCalls(call(ANY, np.ndarray.reshape, self.a, (5, 2)),)

    def test_transpose(self):
        self.trace("self.a.T")
        self.assertCalls(call(ANY, getattr, self.a, "T"))

    def test_concatenate(self):
        self.trace("np.concatenate((self.a, self.a), axis=0)")
        self.assertCalls(
            call(ANY, getattr, np, "concatenate"),
            call(ANY, np.concatenate, (self.a, self.a), axis=0),
        )

    def test_ravel_list(self):
        """
        from numeric function to test array dispatch
        """
        self.trace("np.ravel([1, 2, 3])")
        self.assertCalls(call(ANY, np.ravel, [1, 2, 3]))

    def test_ravel_array(self):
        """
        from numeric function to test array dispatch
        """
        self.trace("np.ravel(self.a)")
        self.assertCalls(call(ANY, np.ravel, self.a))

    def test_std(self):
        self.trace("np.std(self.a)")
        self.assertCalls(call(ANY, np.std, self.a))

    def test_builtin_types_no_call(self):
        self.trace("10 + 10\n12323.234 - 2342.40")
        self.mock.assert_not_called()

    def test_numpy_array_constructor(self):
        self.trace("np.ndarray(dtype='int64', shape=tuple())")
        self.assertCalls(
            call(ANY, getattr, np, "ndarray"),
            call(ANY, np.ndarray, dtype="int64", shape=tuple()),
        )

    def test_contains(self):
        self.trace("1 in self.a")

        self.assertCalls(call(ANY, op.contains, self.a, 1))

    def test_not_contains(self):
        self.trace("1 not in self.a")
        self.assertCalls(call(ANY, op.contains, self.a, 1))

    def test_reduction(self):
        self.trace("np.add.reduce(self.a)")
        self.assertCalls(
            call(ANY, getattr, np, "add"), call(ANY, np.ufunc.reduce, np.add, self.a)
        )

    def test_method(self):
        self.trace("self.a.sum()")
        self.assertCalls(call(ANY, np.ndarray.sum, self.a))

    def test_method_unbound(self):
        self.trace("np.ndarray.sum(self.a)")
        self.assertCalls(
            call(ANY, getattr, np, "ndarray"), call(ANY, np.ndarray.sum, self.a)
        )

    def test_contains(self):
        self.trace("1 in self.a")
        self.trace("self.a in []")
        self.mock.assert_called_once_with(ANY, op.contains, self.a, 1)


class TestMockPandasMethod(BaseTest):
    def setUp(self):
        super().setUp()
        self.tracer = Tracer(["pandas"], ["record_api.test"])
        self.df = pd.DataFrame.from_records([{"hi": 1}])

    def test_from_records(self):
        self.trace("pd.DataFrame.from_records([{'hi': 1}])")
        self.assertCalls(
            call(ANY, getattr, pd, "DataFrame"),
            call(ANY, pd.DataFrame.from_records, [{"hi": 1}]),
        )


if __name__ == "__main__":
    unittest.main()
