"""

input we have given an array 
sort array

"""


def insertinarr(arr,x):

    if arr == [] or arr[-1]<=x:
        arr.append(x)
        return
    last = arr.pop()
    insertinarr(arr,x)
    arr.append(last)
    


def sortarr(arr):
    if len(arr) == 1:
        return 
    x = arr.pop()
    sortarr(arr)
    insertinarr(arr,x) 
    








arr = [2, 3, 7 , 6, 4, 5, 9]
print("old array",arr)
sortarr(arr)
print("new array",arr)
