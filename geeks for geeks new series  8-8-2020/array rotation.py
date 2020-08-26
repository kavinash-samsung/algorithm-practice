# # for array rotation

# array = [1, 2, 3, 4, 5, 6, 7]
# length = len(array)
# d = 2

# # 

n = int(input())
k = int(input())
arr  = list(map(int,input().split()))

lenarray = len(arr)
topop = lenarray-k
for i in range(topop):
    arr.pop(arr.index(min(arr)))
print(min(arr))
