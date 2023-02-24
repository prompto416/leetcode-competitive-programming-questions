

def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    candidates = []
    myDict = dict()
    
    for i in reversed(range(1,len(s))):
        for j in range(len(s)-(i-1)):
            
            temp = s[j:j+i]
            print(temp)
            if temp not in myDict:
                myDict[temp] = 0
            else:
                myDict[temp] += 1
    
    print(myDict)
    # while True:
    candidates = []
    for i in myDict.items():
        if i[1] == max(myDict.values()):
            candidates.append(i)
    for i in range(len(candidates)):
        print(candidates[i][0])
        temp = dict()
        for i in candidates[i][0]:
            if i not in temp:
                temp[i] = None
            if i in candidates[i][0]:
                continue
        
        

            
                
    
  
    
    
            

    
            
        
        
        
    
    
lengthOfLongestSubstring("abcabc")