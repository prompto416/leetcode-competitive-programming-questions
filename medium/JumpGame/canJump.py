def canJump( nums):
    if len(nums) == 1:
        return True
    temp = nums.copy()
    z = [] 
    flag = None
    i = 0 
    while 0 in temp:
        cur_z = temp.index(0)
        z.append(cur_z)
        temp[cur_z] = -1
    if len(z) < 1:
        return True
    
    # while z != []:
    
    while z!= []:
        for i in reversed(range(z[0])):
            distance = z[0] - i
            val = nums[i]
            try:
                
                if (len(z) == 1 and (nums.index(z[0]) == len(nums)-1 )):
                    print(True)
            except:
                print(z[0])
            if val > distance:
                flag = True
                break
            else:
                flag = False
        z.pop()

    return flag

print(canJump([2,0]))