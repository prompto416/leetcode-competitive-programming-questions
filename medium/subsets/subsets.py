def subsets( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i > j:
                res.append([nums[i],nums[j]])
    print(res)
subsets([1,2,3,4])
