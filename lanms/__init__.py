import subprocess
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# print(BASE_DIR)
# if subprocess.call(['nmake', '-C', BASE_DIR]) != 0:  # return value
#     raise RuntimeError('Cannot compile lanms: {}'.format(BASE_DIR))

# Build lanms for windows
# cl adaptor.cpp ./include/clipper/clipper.cpp /I ./include /I "C:\Users\nguye\AppData\Local\Programs\Python\Python37\include" /LD /Fe:adaptor.pyd /link/LIBPATH:"C:\Users\nguye\AppData\Local\Programs\Python\Python37\libs"

def merge_quadrangle_n9(polys, thres=0.3, precision=10000):
    from .adaptor import merge_quadrangle_n9 as nms_impl
    if len(polys) == 0:
        return np.array([], dtype='float32')
    p = polys.copy()
    p[:,:8] *= precision
    ret = np.array(nms_impl(p, thres), dtype='float32')
    ret[:,:8] /= precision
    return ret
