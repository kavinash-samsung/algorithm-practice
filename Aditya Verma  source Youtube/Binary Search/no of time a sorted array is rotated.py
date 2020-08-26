# def findingminimuminsortedarray(array, x):
#     start = 0
#     end = len(array)-1
    
#     while(start <= end):

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
    

array = [5, 6, 7, 8,9, 1, 2, 3, 4]


t = nooftimeasortedarrayisrotated(array)

print(t)








    
