def addToArrayForm(num, k):
    """
    :type num: List[int]
    :type k: int
    :rtype: List[int]
    """
    x = ""
    res = []
    for i in range(len(num)):
        x += str(num[i])
        
    x = str(int(x) + k)
    for i in range(len(x)):
        res.append(int(x[i]))
    
    return res 

        
addToArrayForm([1,2,0,0],34)
        
        