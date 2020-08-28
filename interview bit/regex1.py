def matrixmethod(A,B):

    

s1 = 'acba'
s2 = '*?b*a*a'
print(matrixmethod(s1,s2))
# print(recurse(s1,s2,len(s1),len(s2)))
        


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    
    def isMatch(self, A, B):
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
                    
        l1 = len(A)
        l2 = len(B)
        if l2==0:
            return l1==0
    
        matrix = [[False]*(l2+1) for i in range(l1+1)]
    
        matrix[0][0] = True
    
        for j in range(1, l2+1):
            if B[j-1] == '*':
                matrix[0][j] = matrix[0][j-1]
                
                
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if B[j-1] == '*':
                    matrix[i][j] = matrix[i-1][j] or matrix[i][j-1]
                elif B[j-1] == '?' or B[j-1] == A[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = False
    
        if matrix[l1][l2]:
            return 1
        return 0
         
        
