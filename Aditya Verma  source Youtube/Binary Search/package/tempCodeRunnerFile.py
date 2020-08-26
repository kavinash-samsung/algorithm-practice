
def nooftimeasortedarrayisrotated(array):
    start = 0
    
    n = len(array)

    end = n-1
    
    while(start <= end):
        mid = start + (end-start)//2

        nex = (mid+1)%n
        prev = (n+mid-1)%n
        
        if array[mid] <= array[nex] and array[mid] <= array[prev]:
            return mid
        elif array[mid] >=array[start]:
            start = mid+1
        elif array[mid] <= array[end]:
            end = mid-1
    return -1