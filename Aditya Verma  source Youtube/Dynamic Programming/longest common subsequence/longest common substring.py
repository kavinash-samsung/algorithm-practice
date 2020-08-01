def longestcommonsubstring(string1, string2, lenstring1, lenstring2):
    matrix = [[-1]*(lenstring2+1) for i in range(lenstring1+1)]
    
    for i in range(lenstring2+1):
        matrix[0][i] = 0
    for i in range(lenstring1+1):
        matrix[i][0] = 0
    max_length = 0
    for i in range(1,lenstring1+1):
        for j in range(1,lenstring2+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
                max_length = max(max_length, matrix[i][j])
            else:
                matrix[i][j] = 0
    for i in matrix:
        print(i)
    return max_length

string1 = 'avinashg'
string2 ='ashking'

lenstring1 = len(string1)
lenstring2 = len(string2)
matrix = longestcommonsubstring(string1, string2, lenstring1, lenstring2)

print(matrix)