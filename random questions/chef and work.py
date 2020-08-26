def chef(array,x,cap):
    if array[0]>cap:
        return 0
    reset = 0
    trips = 1
    for i in range(x):
        if array[i] > cap :
            return trips
        if reset+array[i] > cap:
            reset = array[i]
            trips += 1
        else:
            reset += array[i]
    return trips

    
for _ in range(int(input())):
        
    x,cap = tuple(map(int,input().split(" ")))
    array = list(map(int,input().split(" ")))
    print(chef(array,x,cap))

