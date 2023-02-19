def combinationSum( candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    #a list of solutions list with its index being the target length = target+1
    dp = [[] for _ in range(target+1)]
    
    for c in candidates:
        for i in range(1,target+1):
            print(i,c)
            if i < c:continue
            #append basic equal value
            if i == c:
                dp[i].append([c])
                print("append",i,c,dp)
            #append current dp cell with cell[i-c]
            else:
                print("dp[i-c]",dp[i-c])
                #dp[i-c] explanation: for example we have candidate 3 and target is 5 
                #so c=3 and i=5 then 5-3=2 which is the remaning value we need since we already have 3 we need only 2 more 
                #so we pick a previous solution of remaning target=2 in which we have already calculated from previous iteration i=j=2 ; dp[2] = [1,1],[2] (note that dp[target] = solution1,solution2)
                #then we append current dp array(the current target solution array) with previous solution + currentCandidate=target so we get dp[5] = [3,1,1],[3,2] (see that [1,1] and [2] came from above)
                #                                                                                                                             so basically its dp[5] = dp[3]+dp[2] in which dp[2] = 
                for prevSol in dp[i-c]:
                    dp[i].append(prevSol+[c])

    return dp[target]


    
  
   
  
    
        

        
        
print(combinationSum([1,2,3], 5))