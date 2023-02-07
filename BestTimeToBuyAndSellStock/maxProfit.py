
def maxProfit(prices):
    res = 0
    
    for i in range(len(prices)):
        for j in range(len(prices)):
            if  j > i and prices[i] < prices[j] :
                if prices[j] - prices[i] > res:
                    res = prices[j] - prices[i]
               
                
    return res
    
    
    
    
    
    
print(maxProfit([3,2,6,5,0,3]))
