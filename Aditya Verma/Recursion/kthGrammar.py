from math import pow
def kthGrammar(n,k):
    if n==1 or k==1:
        return 0
    mid = pow(2,n-1)//2
    if k <= n:
        return kthGrammar(n-1,k)
    else:
        return int(not kthGrammar(n-1, k))
print(kthGrammar(4,5))
