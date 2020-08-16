from typing import *


class SparseFrameAccessor:
    @classmethod
    def from_spmatrix(cls, /, data: scipy.sparse.csr.csr_matrix):
        """
        usage.sklearn: 1
        """
        ...

    def to_coo(self, /):
        """
        usage.sklearn: 1
        """
        ...
