def floorofanarrayofanelement(array,k):
    start = 0
    end = len(array)-1
    res = -1
    while(start < end):
        mid = start + (end-start)//2
        if array[mid] == k:
            return array[mid]
        elif(array[mid]>k):
            end = mid-1
        elif(array[mid]<k):
            res = array[mid]
            start = mid+1
    return res
        
array = [1,2,3,4,5,6,8]
k = 7

print(floorofanarrayofanelement(array, k))
