def longest_common_subsequence(string1, string2, len_string1, len_string2):
    matrix = [[-1]*(len_string2+1) for i in range(len_string1+1)]

    for i in range(len_string1+1):
        matrix[i][0] = 0
    for j in range(len_string2+1):
        matrix[0][j] = 0
    for i in range(1,len_string1+1):
        for j in range(1, len_string2+1):
            if string1[i-1] == string2[j-1] and i != j:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    for i in matrix:
        print(i)
    return matrix

def printlongestsubsequence(a):
    length = len(a)
    matrix = longest_common_subsequence(a,a,length,length)
    i = j = length
    res_string = ""
    while(i > 0 and j > 0):
        if matrix[i][j] == matrix[i-1][j-1]+1:
            res_string += a[j-1]
            i -= 1
            j -=1
        else:
            j -= 1
    return res_string[::-1]



a = 'aavbbcdd'
length = len(a)
print(printlongestsubsequence(a))

