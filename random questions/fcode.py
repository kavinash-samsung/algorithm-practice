a,k=map(int,input().split())
arr = [0]*a
dictx = dict()
ss = {}
for i in range(a):
    arr[i]=int(input())
    ss[arr[i]] = arr[i]%k 
    if ss[arr[i]] in dictx:
        dictx[ss[arr[i]]] += 1
    else:
        dictx[ss[arr[i]]] = 1

so = sorted(dictx.items(),key=lambda x:x[1],reverse = True)[0][0]
print(dictx[so])
for i in arr:
    if ss[i] == so:
        print(i)








