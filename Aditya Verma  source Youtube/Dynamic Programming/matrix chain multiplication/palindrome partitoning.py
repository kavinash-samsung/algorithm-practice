'''

this is the code for minimum partition for
having all the resultant string as palindrome

in example we have nttina
we have to one partition of this 

from  nittin | a  
now both the resultant string are in palindrome


below is the recursion code of this

'''
print("code using normal recursion")

def palindrome(string):
    return string==string[::-1]

def palindromepartition(string,i,j):
    if i >= j:
        return 0
    if palindrome(string[i:j+1]):
        return 0
    mini = float('inf')
    for k in range(i,j):
        temp = palindromepartition(string,i,k)+palindromepartition(string, k+1, j) + 1

        if mini>temp:
            mini = temp
    return mini

def patrition(string):
    i = 0
    j = len(string)-1
    return palindromepartition(string,i,j)

string = "nitina"

print(patrition(string))

print("first end")
print()

'''


using memoisation with recursion

'''
print("code using recursion and memoisation")

matrix = [[-1]*101 for i in range(101)]
def palindromepartition(string, i, j):
    if i >= j:
        return 0
    if palindrome(string[i:j+1]):
        return 0
    if matrix[i][j] != -1:
        return matrix[i][j]
    mini = float('inf')
    for k in range(i,j):
        temp = palindromepartition(string, i, k)+palindromepartition(string, k+1, j) + 1
        if temp < mini:
            mini = temp
    matrix[i][j] = mini
    return mini


def patrition(string):
    i = 0
    j = len(string)-1
    return palindromepartition(string,i,j)

string = "nitin"

print(patrition(string))

print("recursion memoisation end")

print()

'''

more optimised way to write above code is

'''
print()

print("code using more optimised way recursion and memoisation")

matrix = [[-1]*101 for i in range(101)]
def palindromepartition(string, i, j):
    if i >= j:
        return 0
    if palindrome(string[i:j+1]):
        return 0
    if matrix[i][j] != -1:
        return matrix[i][j]
    mini = float('inf')
    for k in range(i,j):
        
        if matrix[i][k] != -1:
            left = matrix[i][k]
        else:
            left = palindromepartition(string, i, k)
            matrix[i][k] = left
        
        if matrix[k+1][j] != -1:
            right = matrix[k+1][j]
        else:
            right= palindromepartition(string, k+1, j)
            matrix[k+1][j] = right
        
        temp  = 1 + left + right

        if temp < mini:
            mini = temp
    matrix[i][j] = mini
    return mini


def patrition(string):
    i = 0
    j = len(string)-1
    return palindromepartition(string,i,j)

string = "nitina"

print(patrition(string))

print("end this")
