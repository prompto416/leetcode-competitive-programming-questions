def canJump(nums):
    
    lastgood = len(nums)-1
    print(nums,lastgood)
    for i in reversed(range(len(nums)-1)):
        if i + nums[i] >= lastgood:
            print(i,nums[i],lastgood)
            lastgood = i
        print(False,i,nums[i],lastgood)
    return lastgood == 0
nums = [3,2,1,0,4]
canJump(nums)