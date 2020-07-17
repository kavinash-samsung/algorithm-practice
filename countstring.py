

def count(string,char,countn):
    
    if string == '':
        return 0     
    if string[0] ==char:
        return 1+count(string[1:],char,countn)
    return count(string[1:],char,countn)
    
print(count('avinash','a',0))
