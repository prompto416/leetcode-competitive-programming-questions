def isAnagram(s: str, t: str) -> bool:
    
    if len(s) != len(t):
        return False
    myDict = dict()
    res = dict()
    for i in s:
        myDict[i] = 0
    for i in t:
        res[i] = 0
    for i in s:
        if i in myDict:
            myDict[i] += 1
    for i in t:
        if i in res:
            res[i] += 1
    print(myDict)
    print(res)

    return myDict == res

    


   
    
    
    
    
    
    
    
    
    
    
    
    
print(isAnagram("anagram","nagaram"))