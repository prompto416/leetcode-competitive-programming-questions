def topKFrequent( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    
    myDict = dict.fromkeys(nums,0)
    

    for i in range(len(nums)):
     
        if nums[i] in myDict:
            myDict[nums[i]] += 1
            
    
    print(myDict)        
    
    for key,value in myDict.items():
        print(key,value)
    
    i = 0 
    res = []
    while i < k:
        curMax = max(myDict,key=myDict.get)
        res.append(curMax)
        del myDict[curMax]
        i+= 1
   
    return res
  
        
    
    
    
    
topKFrequent([1,1,1,2,2,3],2)