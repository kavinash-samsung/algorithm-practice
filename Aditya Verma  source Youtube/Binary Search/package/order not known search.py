from binary_search import binarysearch
from binary_search_on_reverse_array import binarysearchonreverse

def ordernotknown(array,x):
    if len(array)==1:
        return 0 if array[0] == x else -1

    if array[0]<array[1]:
        return binarysearch(array,x)
    else:
        return binarysearchonreverse(array,x)
