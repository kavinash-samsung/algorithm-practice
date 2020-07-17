'''

induction used for n print to n
for n-1 print n-1

'''

def printn(n):
    if n<=0:
        return
    printn(n-1)
    print(n)

def printnto1(n):
    if n<=0:
        return 0
    print(n)
    printnto1(n-1)

printnto1(100)


"""   Beauty of recursion   """





