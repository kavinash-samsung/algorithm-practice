from package.binary_search import binarysearch
from package.binary_search_on_reverse_array import binarysearchonreverse

def ordernotknown(array,x):
    if len(array)==1:
        return 0 if array[0] == x else -1

    # here we will find out the array is in ascending or descending
    #after finding this we applied particular search

    if array[0]<array[1]:
        return binarysearch(array,x)
    else:
        return binarysearchonreverse(array,x)


arr = [1,2,3,4,5,6,7,8]

print(ordernotknown(arr,5))
    
