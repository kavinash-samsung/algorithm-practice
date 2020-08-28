def numDistinct( string1, string2):
        len_string1 = len(string1)
        len_string2 = len(string2)
        
        matrix = [[-1]*(len_string2+1) for i in range(len_string1+1)]
    
        for i in range(len_string1+1):
            matrix[i][0] = 0
        for j in range(len_string2+1):
            matrix[0][j] = 1
        for i in range(1,len_string1+1):
            for j in range(1, len_string2+1):
                if string1[i-1] == string2[j-1]:
                    matrix[i][j] = matrix[i][j-1] + matrix[i-1][j-1]
                else:
                    matrix[i][j] = matrix[i][j-1]
        
        for i in matrix:
            print(i)
        
        return matrix[len_string1][len_string2]

def recurse(string1,string2,len_string1,len_string2):
    
    if len_string1<0 or len_string2<0 or len_string2<len_string1:
        return 0
    if len_string2 == 0:
        return 1



    if string1[len_string1-1] == string2[len_string2-1]:
        
            
        return recurse(string1, string2, len_string1-1, len_string2-1) + recurse(string1,string2,len_string1,len_string2-1)
    else:
        return recurse(string1,string2,len_string1,len_string2-1)

def numDistincta(a,b):
    return recurse(a,b,len(a),len(b))


a = "rabbit"
b = "rabbbit"
print(numDistinct(a,b))