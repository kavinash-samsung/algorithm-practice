def helper(array):
    if array == "":
        return [""]
    x = array[0]
    res = helper(array[1:])
    witha= []
    without = []

    for i in range(len(res)):
        without.append(x + res[i])
    for i in range(len(res)):
        witha.append("_"+x+res[i])

    return without+witha
    


def outputwithspaces(array):
    x = array[0]
    res = helper(array[1:])
    for i in range(len(res)):
        res[i] = x+res[i]
    return res

print(outputwithspaces('avi'))
