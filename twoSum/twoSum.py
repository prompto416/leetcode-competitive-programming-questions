

def twoSum(nums,target):
    ans = []
    ans += nums
   
    ans.sort()
    
   
    leftPtr = 0
    rightPtr = len(ans)-1
    res = None
    while (leftPtr != rightPtr ):
  
        res = ans[leftPtr] + ans[rightPtr]
        if res > target:
            rightPtr -= 1
        elif res < target:
            leftPtr += 1
        else:
            x = ans[leftPtr]
            y = ans[rightPtr]
            
            a = nums.index(x)
            b = nums.index(y)
            if a == b:
                nums[a] = "buffer"
                b = nums.index(y)
                return [a,b]
            else:
                return [a,b]

        
    return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))
# print(twoSum([3,3],6))
print(twoSum([3,2,3],6))

