def permadd(perm,i):
    for j in range(len(perm)):
        perm[j] = i+perm[j]
def permutation(str):
    if str == "":
        return [""]
    total = []    
    
    for i in range(len(str)):
        perm = permutation(str.replace(str[i],"",1))
        permadd(perm,str[i])
        for i in perm:
            total.append(i)
    return total

print(permutation('avi'))

'''
avi

a   


'''