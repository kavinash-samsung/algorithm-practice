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

print(knapsack(weight, price, capacity, len(weight)))
print(memo)