def longest_common_subsequence(string1, string2, len_string1, len_string2):
    matrix = [[-1]*(len_string2+1) for i in range(len_string1+1)]
    for i in range(len_string1+1):
        matrix[i][0] = 0

    for i in range(len_string2+1):
        matrix[0][i] = 0
    
    for i in range(1, len_string1+1):
        for j in range(1, len_string2+1):
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = 1+matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    return matrix[len_string1][len_string2]

def matchsequencepattern(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)

    lenny = longest_common_subsequence(string1, string2, len_string1, len_string2)
    if lenny == min(len_string1, len_string2):
        return True
    else:
        return False

print("Test Case 1")
print()
print("---------")
print()
string1 = 'reda'
string2 = 'predator'


print(matchsequencepattern(string1, string2))
print()
print("##############################")
print()
print('Test Case 2')

print()
print("---------")
print()

string1 = 'reddit'
string2 = 'predator'


print(matchsequencepattern(string1, string2))




    