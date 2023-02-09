def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a,2)
    b = int(b,2)
    res = bin(a+ b)
    return res[2:]
    
    
    
    
    
    
    
    
    
    
print(addBinary("1010","11"))