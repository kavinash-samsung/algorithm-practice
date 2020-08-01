d = []
count = 0
def solve(n, source, destination, helper,countlist):
    global count
    countlist[0] += 1
    count += 1
    if n == 1:
        d.append((source,destination))
        return 
    solve(n-1, source, helper, destination,countlist)
    d.append((source,destination))
    solve(n-1, helper, destination , source,countlist)
    return count    


def main():
    global count
    n = int(input())
    s = 1
    h = 2
    f = 3
    countlist = [0]
    solve(n,s,h,f,countlist)
    print(countlist[0])
    print(d)
    
main()
print(count)