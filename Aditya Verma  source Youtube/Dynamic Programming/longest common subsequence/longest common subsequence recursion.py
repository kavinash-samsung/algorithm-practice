dicti = {}
def longest_common_subsequence(string1, string2, len_string1,len_string2):
    
    # base case
    if len_string1==0 or len_string2==0:
        return 0
    
    # using memoisation with help of dictionary data type
    if (string1[:len_string1],string2[:len_string2]) in dicti:
        return dicti[(string1[:len_string1],string2[:len_string2])]
    
    # code of choice diagram
    if string1[len_string1-1] == string2[len_string2-1]:
        dicti[(string1[:len_string1],string2[:len_string2])] = 1 + longest_common_subsequence(string1, string2, len_string1-1, len_string2-1)
        return dicti[(string1[:len_string1],string2[:len_string2])]
    else:
        dicti[(string1[:len_string1],string2[:len_string2])] = max(longest_common_subsequence(string1, string2, len_string1-1,len_string2),
                    longest_common_subsequence(string1, string2,len_string1,len_string2-1))
        return dicti[(string1[:len_string1],string2[:len_string2])]


string1 = "avinash"
string2 = 'ashking'
n = len(string1)
m = len(string2)
print(longest_common_subsequence(string1, string2, n, m))