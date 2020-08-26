def binarysearchfirstoccurence(array,x):
    start = 0
    end = len(array)-1
    res = -1
    while(start<=end):
        mid = start +(end-start)//2
        
        if array[mid] == x:
            end = mid-1
            res = mid
        elif array[mid]>x:
            end = mid-1
        else:
            start = mid+1
    return res

def binarysearchlastoccurence(array,x):
    start = 0
    end = len(array)-1
    res = -1
    while(start<=end):
        mid = start +(end-start)//2
        
        if array[mid] == x:
            start = mid+1
            res = mid
        elif array[mid]>x:
            end = mid-1
        else:
            start = mid+1
    return res

arr = [1,2,3,4,4,4,4,4,4,4,5,6,6,6,7,8]


print(binarysearchfirstoccurence(arr,4))
print(binarysearchlastoccurence(arr,6))