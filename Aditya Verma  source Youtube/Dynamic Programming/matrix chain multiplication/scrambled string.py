dict = {}
def scrambled_string(string1, string2):


    if (string1,string2) in dict:
        return dict(string1,string2)

    if len(string1) != len(string2): 
        return False
    # base case 
    n = len(string1)

    if string1 == string2:
        return True

    
    for i in range(1,n):
        if (scrambled_string(string1[0:i], string2[0:i]) and scrambled_string(string1[i:n], string2[i:n])):
        
            dict[(string1,string2)] = True
            return True
        if scrambled_string(string1[0:i], string2[n-i:n]) and scrambled_string(string1[i:n], string2[0:n-i]):
        
            dict[(string1,string2)] = True
            return True
    dict[(string1,string2)] = False
    return False

str1 = 'great'
str2 = 'aterg'

print(scrambled_string(str1, str2))
 

print(dict)