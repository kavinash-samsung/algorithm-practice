import heapq

arr  = [1,4, 5, 2, 1, 2, 4, 4, 5, 4, 2]

def frequencysort(array):
    hashmap = dict()
    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] += 1
        else:
            hashmap[arr[i]] = 1
    print(hashmap)
    maxheap = []
    for x,y in hashmap.items():
        heapq.heappush(maxheap, (-y, -x))
    print(maxheap)
    result = []
    for i in range(len(maxheap)):
        x = heapq.heappop(maxheap)
        result.extend([-x[1]]*(-x[0]))
    print(result)
    

print(frequencysort(arr))