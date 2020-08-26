memo = {}
def knapsack(weight, price, capacity, length):
    if length == 0 or capacity == 0:
        return 0
    if capacity in memo:
        return memo[capacity]
    if weight[length-1] > capacity:
        memo[weight[length-1]] = knapsack(weight, price, capacity, length-1)
        return memo[weight[length-1]]
    else:
        include = price[length-1] + knapsack(weight, price, capacity - weight[length-1], length - 1)
        notinclude = knapsack(weight, price, capacity, length - 1)
        memo[weight[length-1]] = max(include, notinclude)
        return memo[weight[length-1]]
    
price = [10, 40, 20, 50, 22]
weight = [10,20,55,20,40]
capacity = 90

# ar = """57 95 13 29 1 99 34 77 61 23 24 70 73 88 33 61 43 5 41 63 8 67 20 72 98 59 46 58 64 94 97 70 46 81 42 7 1 52 20 54 81 3 73 78 81 11 41 45 18 94 24 82 9 19 59 48 2 72"""
# wt = """83 84 85 76 13 87 2 23 33 82 79 100 88 85 91 78 83 44 4 50 11 68 90 88 73 83 46 16 7 35 76 31 40 49 65 2 18 47 55 38 75 58 86 77 96 94 82 92 10 86 54 49 65 44 77 22 81 52"""

# capacity = 41
# price = list(map(int,ar.split(" ")))
# weight = list(map(int,wt.split(" ")))
# n = print(len(price))
# # def knapsack(item, weight, capacity, n):
# #     if capacity <= 0 or n == 0:
# #         return 0
# #     return max(item[n-1]+knapsack(item, weight, capacity-weight[n-1], n-1),knapsack(item,weight,capacity,n-1))
#     #   item[n-1]
print(knapsack(weight, price, capacity, len(weight)))
# print(memo)