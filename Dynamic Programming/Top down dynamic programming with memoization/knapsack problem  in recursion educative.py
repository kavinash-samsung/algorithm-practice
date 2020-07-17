"""

in this case we have to find every set where 
any object is either in the set or is not
This means we are looking for all the possible subset 
of a set of n objects How many subset exists for a set
of n objects 2**n thus time complexity is O(2^n).



"""


def knapsack(price,weight,capacity,index):
    if capacity <= 0 or index >= len(weight):
        return 0

    if weight[index] > capacity:
        return knapsack(price, weight, capacity, index+1)

    return max(knapsack(weight, price, capacity-weight[index], index+1) + price[index], knapsack(weight, price, capacity, index+1))
def knapsackproblem(price, weight, capacity):
    return knapsack(price, weight, capacity, 0)


def main():
    weight = [2,1,1,3]
    prices = [2,8,1,10]
    capacity = 4                                            
    print(knapsackproblem(weight, prices, capacity))

main()