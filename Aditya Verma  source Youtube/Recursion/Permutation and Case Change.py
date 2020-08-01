def permutation(array):
    if array == "":
        return ['']
    x = array[0]
    res = permutation(array[1:])
    cap = []
    small = []
    for i in range(len(res)):
        small.append(x.lower()+res[i])
    
    for i in range(len(res)):
        cap.append(x.upper()+res[i])
    
    return small+cap
    

print(permutation('ak'))