def permutation(array):
    if array == "":
        return ['']
    x = array[0]
    res = permutation(array[1:])
    cap = []
    small = []
    try:
        if int(x):
            for i in range(len(res)):
                res[i] = x+res[i]
    except ValueError:
                
        for i in range(len(res)):
            small.append(x.lower()+res[i])
        
        for i in range(len(res)):
            cap.append(x.upper()+res[i])
        res = small + cap
        
    return res
    

print(permutation('a1k'))

