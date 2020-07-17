tn=(input())
for i in range(0,tn):
    nm= eval(input())
    lc = list(map(int, input().strip().split()))
    flag = 0
    for i in range(0,nm):
        smb = sum(lc[0:i])
        sma = sum(lc[i+1:])
        if smb!=0 and smb==sma:
            flag=1
            break
        if flag==0:
            print("{} {}".format(0,0))
        else:
            print('{} {}'.format(i+1,sma))