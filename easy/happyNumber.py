def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    if n== 2:
        return False
    
    n_str = str(n)
    while int(n_str) != 1:
        if len(n_str) < 2:
            a = 0
            b = int(n_str)
        else:
            a = int(n_str[0])
            b = int(n_str[1])
        
        n = (a**2) + (b**2)
        n_str = str(n)
        print(a,b)
    
    return True if int(n) == 1 else False
    
    
        
        
        
            
            
             
             
    
    
    
    
    
print(isHappy(2))