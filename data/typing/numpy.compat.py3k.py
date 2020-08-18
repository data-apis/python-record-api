from typing import *


@overload
def asbytes(s: Literal["testdouble\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testdouble"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststring\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststring"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testcomplex\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testcomplex"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testmatrix\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testmatrix"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testsparse\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testsparse"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testsparsecomplex\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testsparsecomplex"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["theta\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["a\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["theta"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["a"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["testminus\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testminus"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testonechar\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testonechar"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testcell"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testscalarcell"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testemptycell"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststringarray"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["test3dmatrix"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststruct"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testcellnest"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststructnest"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["teststructarr"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testobject"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testunicode"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testbools"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testobjectarray"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["x\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["x"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["d"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["longstruct"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["aaaaa"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["aaaa"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["aaaaaa"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["dict"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["oned\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["oned"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["arr"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["arr2"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["A"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["c"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["floats"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["ints"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["uni_arr"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["barray"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testfunc"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["st"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["scalar"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["string"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["mystr"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["mynum"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["second_cat\x00"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: str):
    """
    usage.scipy: 8
    """
    ...


@overload
def asbytes(s: Literal["%\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["1\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["4\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["2147483647\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2147483645\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2147483646\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2147483644\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2147483648\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["9223372036854775806\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["4294967296\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["9223372036854775807\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["0\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["5\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["6\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["3 2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["-2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["-2.00000000e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["20 20\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["20 15\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 4\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["1 1 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2 2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 1 2147483647\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2 -2147483646\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 2147483645\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 2147483644\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 1 4294967297\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2 4294967297\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2 2147483646\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 3 6\n"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["1 3 3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 4\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 5\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["3 2 6\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 -2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 1 1.0000000e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1 -2.0000000e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 2 4.0000000e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["20 20 210\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["20 15 300\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1 2\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["2 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["10 10 0\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["5 5 8\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 3e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 3.1e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 3.14e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["10001 10001 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["100001 100001 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1000001 1000001 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["10000001 10000001 1\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e+00\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-01\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-01\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-01\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-02\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-02\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-02\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-03\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-03\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-03\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-04\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-04\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-04\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-05\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-05\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-05\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-06\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-06\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-06\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-07\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-07\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-07\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-08\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-08\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-08\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["11 11 1e-09\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["101 101 1.0e-09\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["1001 1001 1.00e-09\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["time"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["history"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: bytes):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["units"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["appendRan"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["app_dim"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["app_var"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["dim"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["var"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["_FillValue"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["v"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["v1"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["v2"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["v3"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["float_var"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["zerodim"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["holy"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["witch"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["Kilroy"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["naughty"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["y"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["testData"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["data"]):
    """
    usage.scipy: 2
    """
    ...


@overload
def asbytes(s: Literal["Temperature"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["missing_value"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["scale_factor"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["add_offset"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["3 3 3\n"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["libg2c"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asbytes(s: Literal["libgfortran"]):
    """
    usage.scipy: 1
    """
    ...


def asbytes(s: Union[str, bytes]):
    """
    usage.scipy: 203
    """
    ...


@overload
def asstr(s: bytes):
    """
    usage.scipy: 11
    """
    ...


@overload
def asstr(s: Literal["%%MatrixMarket"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asstr(s: Literal["matrix"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asstr(s: Literal["coordinate"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asstr(s: Literal["complex"]):
    """
    usage.scipy: 1
    """
    ...


@overload
def asstr(s: Literal["symmetric"]):
    """
    usage.scipy: 1
    """
    ...


def asstr(
    s: Union[
        Literal["symmetric", "complex", "coordinate", "matrix", "%%MatrixMarket"], bytes
    ]
):
    """
    usage.scipy: 16
    """
    ...
