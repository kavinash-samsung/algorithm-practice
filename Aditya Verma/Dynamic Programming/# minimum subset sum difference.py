def sumsubset(array, sumn, length):
    matrix = [[False]*(sumn+1) for i in range(length+1)]
    for j in range(sumn+1):
        matrix[0][j] = False
    for j in range(length+1):
        matrix[j][0] = True
    for i in range(1, length+1):
        for j in range(1, sumn+1):
            if j >= array[i-1]:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-array[i-1]]
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[length][sumn]

def mindifference(array,length):
    total_range = sum(array)
    half_range = total_range//2
    min_candidates = []
    for i in range(1,half_range+1):
        if sumsubset(array, i, length) == True:
            min_candidates.append(i)
    s1 =  max(min_candidates)
    s2 = total_range - s1
    return s2-s1

array = [1,5,11,5,1]
length = len(array)
print(mindifference(array,length))

