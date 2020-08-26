matrix = []

def solve(e, f):
    if f == 0 or f==1:
        return f
    if e == 1:
        return f
    if matrix[e][f] != -1:
        return matrix[e][f]

        
    mn = float('inf')

    for i in range(1,f+1):

        temp = 1+ max(solve(e-1,i-1), solve(e,f-i))

        mn = min(temp,mn)
    matrix[e][f] = mn
    return matrix[e][f]


def main():
    e = 3
    f = 20
    global matrix
    matrix = [[-1]*(f+1) for i in range(e+1)]

    print(solve(e,f))

main()