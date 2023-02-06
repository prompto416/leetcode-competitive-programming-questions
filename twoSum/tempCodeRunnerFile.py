

def twoSum(nums,target):
    
    nums.sort()
    
    print(nums)
    
    leftPtr = 0
    rightPtr = len(nums)-1
    res = None
    while (leftPtr != rightPtr ):
        res = nums[leftPtr] + nums[rightPtr]
        print(res)
        if res > target:
            rightPtr -= 1
        elif res < target:
            leftPtr += 1
        else:
            return [leftPtr, rightPtr]
        
    return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,3],6))

print(twoSum([3,2,4],6))