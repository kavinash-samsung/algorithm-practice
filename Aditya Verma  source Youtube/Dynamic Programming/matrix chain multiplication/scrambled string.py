dictx = {}
def scrambled_string(string1, string2):


    if (string1,string2) in dictx:
        return dictx(string1,string2)

    if len(string1) != len(string2): 
        return False
    # base case 
    n = len(string1)

    if string1 == string2:
        return True

    
    for i in range(1,n):
        if (scrambled_string(string1[0:i], string2[0:i]) and scrambled_string(string1[i:n], string2[i:n])):
        
            dictx[(string1,string2)] = True
            return True
        if scrambled_string(string1[0:i], string2[n-i:n]) and scrambled_string(string1[i:n], string2[0:n-i]):
        
            dictx[(string1,string2)] = True
            return True
    dictx[(string1,string2)] = False
    return False



str1 = 'great'
str2 = 'aterg'

print(scrambled_string(str1, str2))
 

