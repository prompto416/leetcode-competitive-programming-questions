
def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    y = str(x)
    x = str(x)
    x = x[::-1]
    print(x,y)
    quit()
    if x == y:
        return True 
    else:
      return False
    
    
    
isPalindrome(-123)