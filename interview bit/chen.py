def recurse(string1, string2, masterstring, l1 ,l2 , lenmaster):
    if lenmaster == 0:
        return 1
    if l1 <= 0 and l2 <= 0:
        return 0 
    up = 0
    down = 0
    if l1 >=1 and string1[l1-1] == masterstring[lenmaster-1]:
        up = recurse(string1, string2, masterstring, l1-1, l2, lenmaster-1)
    if l2 >= 1 and string2[l2-1] == masterstring[lenmaster-1]:
            down = recurse(string1, string2, masterstring, l1, l2-1, lenmaster-1)

    # if string1[l1-1] == masterstring[lenmaster-1] or string2[l2-1] == masterstring[lenmaster-1]:
    #     up = False
    #     down = False
    if up or down :
        return 1   
    return 0

s1 = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
s2 = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
s3 = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

print(recurse(s1, s2, s3, l1, l2, l3))
