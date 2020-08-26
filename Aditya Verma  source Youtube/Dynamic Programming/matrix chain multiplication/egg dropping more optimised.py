matrix = []

def solve(e, f):
    if f == 0 or f==1:
        return f
    if e == 1:
        return f
    if matrix[e][f] != -1:
        return matrix[e][f]

        
    mn = float('inf')

    for k in range(1,f+1):
        if matrix[e-1][k-1] != -1:
            low = matrix[e-1][k-1]
        else:
            low = solve(e-1,k-1)
            matrix[e-1][k-1] = low


        if matrix[e][f-k] != -1:
            high = matrix[e][f-k]
        else:
            high = solve(e,f-k)
            matrix[e][f-k] = high

        temp = 1+ max(low,high)

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