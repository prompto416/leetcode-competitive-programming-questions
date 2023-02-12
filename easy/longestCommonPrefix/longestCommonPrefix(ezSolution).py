


#use first string as a pivot and compare it with the rest
#keep deleting the last letter of the pivot until it matches with the rest
#if no common prefix are found it will stop when it becomes an empty string
def longestCommonPrefix(strs):
    res = ""
    s = strs
    prefix = strs[0]
    
    if len(strs) == 0:
        return ""
    for i in range(1,len(s)):
        #empty string is subset of every string so while loop will eventually stop
        while s[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix)-1]
            
    
    
 
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))