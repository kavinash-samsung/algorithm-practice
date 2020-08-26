from first_and_last_occurrence import binarysearchfirstoccurence, binarysearchlastoccurence


def countofanelementinsortedarray(array,x):
    
    first = binarysearchfirstoccurence(array,x)
    last = binarysearchlastoccurence(array,x)
    return last-first+1