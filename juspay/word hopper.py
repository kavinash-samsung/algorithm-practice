

# def lcs(string1, string2, len_string1, len_string2):
#     matrix = [[-1]*(len_string2+1) for i in range(len_string1+1)]

#     for i in range(len_string1+1):
#         matrix[i][0] = 0
#     for j in range(len_string2+1):
#         matrix[0][j] = 0
#     for i in range(1,len_string1+1):
#         for j in range(1, len_string2+1):
#             if string1[i-1] == string2[j-1]:
#                 matrix[i][j] = 1 + matrix[i-1][j-1]
#             else:
#                 matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    
#     return matrix[len_string1][len_string2]


# a = 'git'
# b= 'dog'
# n = 6
# arr = ['log','fog','mot','pkm','dog','got']


# temp = a
# fin = b
# hop = 0
# flag = 0

# while (len(temp)-lcs(temp,fin,3,3) != 1):
#     flag = 1
#     for i in arr:
#         if (len(temp)-lcs(temp, i, 3, 3) == 1):
#             temp = i
#             hop += 1
#             flag = 0
#             break

# if flag == 0:
#     print(hop+1)
# else:
#     print(-1)












input_from_question = '4'


a = int(input_from_question)
b= []
for i in range(a):
    b.append(list(input()))
print(b)

for i in range(a):
    for j in range(b):
        b[i][j] = int(b[i][j])


s = 0
for i in b:
    s += len(b)-sum(i)-1

print(s)









 