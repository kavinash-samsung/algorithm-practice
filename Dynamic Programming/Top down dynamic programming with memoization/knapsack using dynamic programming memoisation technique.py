"""
in this we are storing too many results 
in our hashset sunce we are only evaluating 
and storing as many results as we need in the 
memo table 
the rest will be O(1) lookup from it.

The index can go 1 to n
and capacity will go to zero 
capacity cannot be less then it so
the size of hashset will be c*n
c-capacity
n-elements present

Time complexity if O(C*n)


"""

dicti = {}
def knapsack(weight, price, capacity, index):
    if index >= len(weight) or capacity <= 0:
        return 0
    if (capacity,index) in dicti:
        return dicti[(capacity,index)]
    if  weight[index] > capacity:
        dicti[(capacity,index)] = knapsack(weight, price, capacity, index+1)
        return dicti[(capacity, index)]
        
    dicti[(capacity,index)] = max(price[index]+knapsack(weight, price, capacity-weight[index], index+1), 
    knapsack(weight, price, capacity, index+1))

    return dicti[(capacity,index)]
    

def implementknapsack(weight, price, capacity):
    return knapsack(weight, price, capacity, 0)


def main():
    price = [2,8,1,10]
    weight = [2,1,1,3]
    capacity = 4
    print(implementknapsack(weight,price,capacity))


main()