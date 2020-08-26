import heapq
def kthsmallestelement(array,k):
     arr = []
     heapq.heapify(array)
     for i in range(len(array)):
         heapq.heappush(arr,-array[i])
         if len(arr)>k:
             d = heapq.heappop(arr)
            #  print(d)
     return -heapq.heappop(arr)

k = 3
arr = [3,5,4,6,8,5,2]

print(kthsmallestelement(arr,k))     
     