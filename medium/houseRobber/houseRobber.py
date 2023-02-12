

def rob(nums):
    print(nums)
    dp = []
    for i in range(len(nums)+1):
        dp.append(0)

    dp[1] = nums[0]
    print(dp)


    for i in range(1,len(nums)):
        dp[i+1] = max(dp[i],dp[i-1] + nums[i])
        print("i",i,dp,dp[i],"or",dp[i-1],"+",nums[i])



print(rob([1,3,1,3,100]))