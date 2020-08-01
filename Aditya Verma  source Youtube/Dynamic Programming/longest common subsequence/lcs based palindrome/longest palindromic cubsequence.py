def longest_common_subsequence(string1, string2, len_string1, len_string2):
    matrix = [[-1]*(len_string2+1) for i in range(len_string1+1)]

    for i in range(len_string1+1):
        matrix[i][0] = 0
    for j in range(len_string2+1):
        matrix[0][j] = 0
    for i in range(1,len_string1+1):
        for j in range(1, len_string2+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    for i in matrix:
        print(i)
    return matrix

def longestpalindromiccubsequence(string1):
    a = string1
    b = a[::-1]
    length = len(a)
    matrix = longest_common_subsequence(a,b,length,length) 
    print("length of palindromic subsequence", matrix[length][length])
    i = j = length
    result_string = ""
    while(i>0 and j>0):
        if a[i-1] == b[j-1]:
            result_string += a[i-1]
            i -= 1
            j -= 1
        else:
            if matrix[i-1][j]> matrix[i][j-1]:
                i -= 1
            else:
                j -= 1
    return result_string[::-1]
string = 'predator'
print(longestpalindromiccubsequence(string))