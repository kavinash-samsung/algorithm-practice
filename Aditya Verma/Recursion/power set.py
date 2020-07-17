def powerSet(array, result):
    if array == []:
        return [[]]
    x = array[0]
    left = powerSet(array[1:], result)
    right = powerSet(array[1:], result)
    for i in range(len(right)):
        right[i] = [x] + right[i]
        
    return right+left
    
    
    
    


result = []
array = [1,2,3]
print(powerSet(array,result))