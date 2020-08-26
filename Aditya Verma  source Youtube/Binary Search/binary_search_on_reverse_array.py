def binarysearchonreverse(array,x):
    start = 0
    end = len(array)-1
    
    while(start<=end):
        mid = start +(end-start)//2
        if array[mid] == x:
            return mid
        elif array[mid]>x:
            start = mid+1
        else:
            end = mid-1
    return -1





arr = [8, 7, 6, 5, 4, 3, 2, 1]


print(binarysearchonreverse(arr,7))