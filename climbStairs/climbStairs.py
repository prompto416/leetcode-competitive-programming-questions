

def climbStairs(n):
    if n == 1 or n == 2:
        return n 
    n2 = 2
    n1 = 1
    res = 0
    count = 2
    while count < n:
        res = n2+n1
        n1 = n2 
        n2 = res
        print(res,n1,n2)
        count += 1
    return res
        
        
        
    
    
    
    
    
# print(climbStairs(3))    
# print(climbStairs(4))   
print(climbStairs(6))  

