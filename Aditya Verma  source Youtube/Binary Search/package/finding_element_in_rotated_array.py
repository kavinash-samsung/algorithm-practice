from package.no_of_time_array_is_rotated import nooftimeasortedarrayisrotated
from package.binary_search import binarysearch

def findingelementinrotatedarray(array,k):
    x = nooftimeasortedarrayisrotated(array)
    # print(x)
    left = array[:x]
    right = array[x:]
    l = binarysearch(left, k)
    r = binarysearch(right, k)
    if l == -1:
        return x+r
    else:
        return l