# def matrixmethod(A,B):

    

# s1 = 'acba'
# s2 = '*?b*a*a'
# print(matrixmethod(s1,s2))
# # print(recurse(s1,s2,len(s1),len(s2)))
        


def isMatch(A, B):
    t = ""
    for i in range(len(B)):
        if B[i] != '*':
            t += B[i]
        else:
            if t != "" and t[-1] != '*':
                t+=B[i]
            elif t == "":
                t += '*'
    B=t
    A = 'X' + A
    B = 'X' + B
    l1 = len(A)
    l2 = len(B)
    
    
    if l2==1:
        return l1==1            
    
    if l1 == 1:
        A = " X"
        l1 = 2

    matrix = [[False]*(l2+1) for i in range(l1+1)]

    matrix[0][0] = True


            
            
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if B[j-1] == '*':
                matrix[i][j] = matrix[i][j-2] or ((A[i-1]==B[j-2] or B[j-2] == ".") and matrix[i-1][j])
            elif B[j-1] == '.' or B[j-1] == A[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = False

    for i in matrix:
        print(i)
    
    if matrix[l1][l2]:
        return 1
    return 0


    
a = 'abcbcd'
b = 'a.*c.*d'
print(isMatch(a,b))