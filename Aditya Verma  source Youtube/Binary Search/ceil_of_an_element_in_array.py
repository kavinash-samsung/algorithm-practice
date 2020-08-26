def ceilofanelement(array, k):
    start = 0
    end = len(array) - 1
    res = 0

    while(start < end):
        mid = start + (end - start)//2

        if array[mid] == k:
            return array[mid]
        elif array[mid]<k:
            start = mid+1
        elif array[mid]> k:
            res = array[mid]
            end = mid-1
    return res

array = [1,2,3,4,5,6,8,9,10]
k = 7
print(ceilofanelement(array,k))
