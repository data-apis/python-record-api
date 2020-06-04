

def isMaskedArray(x: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
    'usage.skimage: 18'

def array(data: numpy.ndarray, mask: Union[(list[list[int]], bool, numpy.ndarray)], fill_value: Union[(float, numpy.float64)]=...):
    'usage.skimage: 7'

def getdata(a: Union[(numpy.ma.core.MaskedArray, numpy.ndarray)]):
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
