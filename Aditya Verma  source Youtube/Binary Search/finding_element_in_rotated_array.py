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


# def nooftimeasortedarrayisrotated(array):
#     start = 0
    
#     n = len(array)

#     end = n-1

#     while(start < end):
#         mid = start + (end-start)//2
#         if array[mid] == array[end]:
#             end -= 1
#         elif array[mid]<=array[end]:
#             end = mid
#         else:
#             start = mid+1
#     return end

array = [5, 6, 7, 8, 1, 2, 3, 4]
k = 3
print(findingelementinrotatedarray(array, k))
    