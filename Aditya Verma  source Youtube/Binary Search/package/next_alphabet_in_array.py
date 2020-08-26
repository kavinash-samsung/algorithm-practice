def nextalphabetinarray(array,k):
    start = 0
    end = len(array) - 1
    res = -1
    while(start<end):
        mid = start +(end-start)//2

        if array[mid] == k:
            return array[mid+1]
        elif array[mid] > k :
            res = array[mid]
            end = mid-1
        elif array[mid] < k:
            start = mid+1
    return res