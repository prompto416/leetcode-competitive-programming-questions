def longestCommonSubsequence(text1: str, text2: str) -> int:
    
    # m,n = len(text1), len(text2)
    # dp = [[0]*(m+1) for _ in range(n+1)]
    l = max(len(text1), len(text2))
    s = min(len(text1), len(text2))
    longStr,shortStr = None,None
    if len(text1) > len(text2):
        longStr = text1
        shortStr = text2
    else:
        longStr = text2
        shortStr = text1
    dp = []
    
    for i in range(s+1):
        temp = [0] * (l+1)
        dp.append(temp)
        
    for i in range(1,s+1):
        for j in range(1,l+1):
            print(i,j,shortStr[i-1],longStr[j-1])
            if shortStr[i-1] == longStr[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i-1][j],dp[i][j-1])

    return(dp[s][l])
    
    
    #  def longestCommonSubsequence(self,text1: str, text2: str) -> int:
    
    #     m,n = len(text1), len(text2)
    #     dp = [[0]*(m+1) for _ in range(n+1)]
    #     print(dp)
    #     for i in range(1,n+1):
    #         for j in range(1,m+1):
    #             if text2[i-1] == text1[j-1]:
    #                 dp[i][j] = 1 + dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    #     return dp[-1][-1]
    
    
    #2D array represnting rows and columns of the table above 
    #     ""  a  b  c  d  e
    # ""[[0, 0, 0, 0, 0, 0],
    # a  [0, 1, 1, 1, 1, 1], 
    # c  [0, 1, 1, 2, 2, 2], 
    # e  [0, 1, 1, 2, 2, 3]]
    # 
    # if chr(i) == char(j) {cur += 1} 
    # else if chr(i) != char(j) 
    # && up != null || left != null {cur = (max(up,left))}


print(longestCommonSubsequence("bsbininm","ace"))