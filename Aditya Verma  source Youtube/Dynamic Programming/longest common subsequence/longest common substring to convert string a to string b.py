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
    
    return matrix[len_string1][len_string2]


def insertiondeletion(string1, string2):    
    len_string1 = len(string1)
    len_string2 = len(string2)

    lcs = longest_common_subsequence(string1, string2, len_string1, len_string2)
    res = len_string1-lcs
    print("deletion requires",res)
    print("insertion required", len_string2-res)


string1 = 'heap'
string2 = 'pea'
insertiondeletion(string1, string2)