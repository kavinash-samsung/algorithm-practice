from package.first_and_last_occurrence import binarysearchfirstoccurence, binarysearchlastoccurence


def countofanelementinsortedarray(array,x):
    
    first = binarysearchfirstoccurence(array,x)
    last = binarysearchlastoccurence(array,x)
    return last-first+1


array = [1,2,3,4,4,4,4,4,4,5,6,7,8]
x = 4
print(countofanelementinsortedarray(array, x))