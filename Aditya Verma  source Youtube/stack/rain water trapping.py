'''
    |
|   |
| | |
|||||

rain water trapped in this is - 5

'''


buildings = [3, 1, 2, 1, 4]
n = len(buildings)
lmax = [0]*n
rmax = [0]*n
lmax[0] = buildings[0]
rmax[n-1] = buildings[n-1]
result = [0]*n

for i in range(1,n):
    lmax[i] = max(buildings[i],lmax[i-1])
    rmax[n-i-1] = max(buildings[n-i-1],rmax[n-i])


for i in range(n):
    result[i] = min(lmax[i], rmax[i]) - buildings[i]


# # for j in range(n-1,0,-1):
# #     rmax = max(buildings[i],buildings[i-1])
# print(lmax)
# print(rmax)
# print("yes")


print(result)

print(sum(result))





