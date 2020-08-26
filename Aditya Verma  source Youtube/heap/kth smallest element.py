import heapq
array = [7, 10, 4, 3, 20, 15]

def kthsmallestelement(array, k):
    maxheap = []
    for i in array:
        heapq.heappush(maxheap, i)
        if len(maxheap)>k :
            heapq.heappop(array)
    return heapq.heappop(array)

print(kthsmallestelement(array,3))