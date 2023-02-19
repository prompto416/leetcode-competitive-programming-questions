def longestConsecutive( nums: list) -> int:
    numSet = set(nums)
    print(numSet)
    
    longest = 0
    
    for n in numSet:
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(longest,length)
            
    return longest
            
#[1,2,3,4,100,200]
    
    
        
            
            
            
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1,100,200]))
print(longestConsecutive([100,4,200,1,3,2]))