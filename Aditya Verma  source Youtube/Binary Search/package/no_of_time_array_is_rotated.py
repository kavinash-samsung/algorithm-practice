def nooftimeasortedarrayisrotated(array):
    start = 0
    
    n = len(array)

    end = n-1

    while(start < end):
        mid = start + (end-start)//2
        if array[mid] == array[end]:
            end -= 1
        elif array[mid]<=array[end]:
            end = mid
        else:
            start = mid+1
    return end
    


