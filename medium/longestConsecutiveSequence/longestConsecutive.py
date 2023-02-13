def longestConsecutive( nums: list) -> int:
        nums.sort()
        if len(nums) == 1:
            return 1 
        elif len(nums) == 2 and abs(nums[0]-nums[1])== 1:
            return 2
        start = False
        mem = []
        print(nums)
        for i in range(len(nums)-1):
            if abs(nums[i+1] - nums[i]) == 1 and start == False:
                mem.append(i)
                start = True
            elif start == True and nums[i+1] - nums[i] !=1:
                mem.append(i)
                start= False
            elif i == len(nums)-2 :
                print(i,len(nums)-2)
                mem.append(i)
            
        print(mem)
        return max(mem)
            
            
            
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))