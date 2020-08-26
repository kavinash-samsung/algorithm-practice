from package.binary_search import binarysearch
def findingposininfinitearray(array, n):
    end = 1
    while(array[end]<n):
        end = end*2
    start = end//2
    startrem = start
    pos_in_remaining_array = binarysearch(array[start:end+1], n)
    return startrem+pos_in_remaining_array


array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

k = 10


print(findingposininfinitearray(array,k))


    