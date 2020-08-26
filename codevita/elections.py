def givecount(st,queue):
    for i in range(len(queue)):
        if queue[i] != '-' :
            if queue[i] == 'st':
                return i+1
            return 0
    

    
lenqueue = 14
queue = '--AB--AB---A--'
count_a = 0
count_b = 0
opqueue = queue[::-1]
count_a = givecount('A',queue)
count_b = givecount('B',opqueue)

if count_a>count_b:
    print('A')
elif count_b>count_a:
    print('B')
else:
    print('coalition')