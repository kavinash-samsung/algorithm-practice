


# def goodsequence(array):
#     n = len(array)//2

#     s1 = array[:n]
#     s2 = array[n:]
    
#     # maxi = max(s1)
#     # mini = max(s2)
    
#     if min(s1) > max(s2) or max(s1)<min(s2):
#         return True
#     else:
#         return False
    
# def total(array):
#     n = len(array)
#     listi = []
#     for i in range(len(array)+1):
#         for j in range(i+2,n+1,2):
#             listi.append(array[i:j])
#     count = 0
#     for i in listi:
#         if goodsequence(i):
#             count += 1
#     return count
    



# array = [1,3,2,4]
# # print(goodsequence([2,3]))

# print(total(array))




    

# cook your dish here


def goodsequence(array):
    n = len(array)//2

    s1 = array[:n]
    s2 = array[n:]
    
    # maxi = max(s1)
    # mini = max(s2)
    
    if min(s1) > max(s2) or max(s1)<min(s2):
        return True
    else:
        return False
    
def total(array):
    n = len(array)
    listi = []
    for i in range(len(array)+1):
        for j in range(i+2,n+1,2):
            listi.append(array[i:j])
    count = 0
    for i in listi:
        if goodsequence(i):
            count += 1
    return count
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = 0
    for i in range(n-1):
        x = total(arr)
        maxi = max(maxi,x)
        arr.append(arr.pop(0))
    print(maxi)

