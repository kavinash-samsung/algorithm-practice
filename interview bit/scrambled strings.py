

def scrambled_string(a,b):
    if len(a)!= len(b):
        return False
    n = len(a)
    if a==b:
        return True
    
    for i in range(1,n):
        if scrambled_string(a[:i],b[:i]) and scrambled_string(a[i:],b[i:]):
            return True
        elif scrambled_string(a[:i],b[n-i:]) and scrambled_string(a[i:],b[:n-i]) :
            return True
        
    return False


print(scrambled_string('avinash','ashinva'))