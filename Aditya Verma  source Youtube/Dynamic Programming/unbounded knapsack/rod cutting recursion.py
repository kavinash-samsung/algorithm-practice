'''

this is the naive approach for this solution
the time complexity using recursion is O(n^3)

we cant use memoisation in this because 
the value will overlapp and change the previous value 
which leads to the wrong memory


'''



def knapsack1(weight, price, capacity, length):
    if length == 0 or capacity == 0:
        return 0

    if weight[length-1] > capacity:
        return knapsack1(weight, price, capacity, length-1)
       
    else:
        include = price[length-1] + knapsack1(weight, price, capacity - weight[length-1], length)
        notinclude = knapsack1(weight, price, capacity, length - 1)
    return max(include, notinclude)
        

length_array = [1,2,3,4,5,6,7,8]
value_array = [9,7,6,5,71,3,2,1]

n = 8


print(knapsack1(length_array, value_array,n,8))
