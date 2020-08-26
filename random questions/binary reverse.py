finallist = []


def reverseBits(num, bitSize):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse)) * '0'
    r = int(reverse, 2)

    finallist.append(r)
    return r


try:

    input1 = input()
    while input1 != "":
        num = int(input1)
        bitSize = 32
        reverseBits(num, bitSize)
        input1 = input()
        
except:
    pass

for i in range(len(finallist) - 1):
    print(str(finallist[i]) + ',', end='')

print(str(finallist[-1]))