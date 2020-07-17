'''

In this algorithm we reduces 
the space complexity of this complexity 
y storing that only information which is necessary
we only stored two variabls instead of whole list  

'''

def fibonicci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    secondLast = 0
    last = 1
    current = None
    for i in range(1,n):
        current = secondLast + last
        secondLast = last
        last = current
    return current

print(fibonicci(6))        