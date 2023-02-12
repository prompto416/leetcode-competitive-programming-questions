#pinned solution
def maxProfit(prices):
    # for some reason leetcode give me array of length =1 
    if len(prices) < 2:
        return 0
    leftPtr = 0
    rightPtr = 1
    profit = prices[rightPtr] - prices[leftPtr]
    i = 0 
    while i < len(prices)-1:
        #currentProfit is the profit of the current pair (current iteration)
        left = prices[leftPtr]
        right = prices[rightPtr]
        
        currentProfit = right - left
        print(left,right,currentProfit)
        if left > right:
            leftPtr = rightPtr 
            rightPtr += 1
        else:
            rightPtr += 1
        if currentProfit > profit:
            profit = currentProfit
        
            
        
        i+= 1
    #in case it is non profitable
    if profit < 0:
        return 0 
    return profit
    
    
    
    
    
    
print(maxProfit([3,2,6,5,0,3]))
# print(maxProfit([7,1,5,3,6,4]))
