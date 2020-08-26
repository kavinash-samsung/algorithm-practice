def searchingelementinnearlysortedarray(array,k):
    start = 0
    end = len(array)-1
    while(start < end):
        mid = start + (end-start)//2
        if array[mid] == k:
            return mid
        
        if mid-1>start and array[mid-1] == k:
            return mid-1
        
        if mid+1 <= end and array[mid+1] == k:
            return mid+1
        
        if array[mid] < k:
            start = mid + 2

        elif array[mid] > k:
            end = mid - 2

