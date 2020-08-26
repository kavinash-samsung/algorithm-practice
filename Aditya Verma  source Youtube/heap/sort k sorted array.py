import heapq


def ksortedarray(array,k):
    n = len(array)
    minheap = []
    for i in range(n):
        heapq.heappush(minheap,array[i])
        if len(minheap)>k:
            x = heapq.heappop(minheap)
            array[i-k] = x
    

    while(minheap != []):
        x = heapq.heappop(minheap)
        array[n-k] = x
        k -= 1
    return array

array = [6, 5, 3, 2, 8, 10, 9]
k = 3

ksortedarray(array,3)
print(array)
        