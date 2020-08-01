def longestcommonsubsequence(string1, string2, string_len1, string_len2):
    matrix = [[0]*(string_len2+1) for i in range(string_len1+1)]
    for i in range(string_len1+1):
        matrix[i][0] = 0
    for j in range(string_len2+1):
        matrix[0][j] = 0
    for i in range(1,string_len1+1):
        for j in range(1,string_len2+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    i = string_len1
    j = string_len2


    resstring = ""
    while(i>0 and j>0):
        if string1[i-1] == string2[j-1]:
            resstring = string1[i-1] + resstring
            i -= 1
            j -= 1
        else:
            if matrix[i-1][j] > matrix[i][j-1]:
                i -= 1
            else:
                j -= 1
    return resstring
                 


string1 = 'avinashg'
string2 = 'ashkg'

string_len1 = len(string1)
string_len2 = len(string2)

matty = longestcommonsubsequence(string1, string2, string_len1, string_len2)

print(matty)

# for i in matty:
#     print(i)