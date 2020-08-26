import heapq

def knearestno(array, x, k):
    k += 1
    n = len(array)
    absdiff = []
    maxheap = []
    for i in range(n):
        absdiff.append(abs(array[i]-x))
    

    for i in range(n):
        heapq.heappush(maxheap,(-absdiff[i],array[i]))
        
        if len(maxheap)>k:
            heapq.heappop(maxheap)
    
    n = []
    while(maxheap):
        n.append(heapq.heappop(maxheap)[1])
    n.remove(x)
    return n

array = [5,6,7,8,9]
k = 3
x = 7

print(knearestno(array, x, k))



    
     