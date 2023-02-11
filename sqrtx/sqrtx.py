def mySqrt( x):
        """
        :type x: int
        :rtype: int
        """
        i = 1
        while True:
            if (i*i == x):
                return i 
            if (i*i > x):
                return i-1
            i+= 1 
            
print(mySqrt(9))