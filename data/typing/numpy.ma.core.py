

def isMaskedArray(x: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    'usage.skimage: 18'

def array(data: numpy.ndarray, mask: Union[(numpy.ndarray, bool, list[list[int]])], fill_value: Union[(numpy.float64, float)]=...):
    'usage.skimage: 7'

def getdata(a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]):
    'usage.skimage: 3'

def getmaskarray(arr: numpy.ma.core.MaskedArray):
    'usage.skimage: 1'

def MaskedArray.mean(self: numpy.ma.core.MaskedArray):
    'usage.skimage: 1'

def MaskedArray.reshape(self: numpy.ma.core.MaskedArray, *s: Literal[('v', 't')]):
    'usage.skimage: 1'

class MaskedArray():
    ndim = ...
    shape = ...
    fill_value = ...
    mask = ...
