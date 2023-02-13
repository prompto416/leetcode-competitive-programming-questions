def twoSum(numbers,target) -> List[int]:
        num = numbers
        p1 = 0
        p2 = len(numbers)-1
        res = None
        while p1 != p2:
            res = num[p1] + num[p2]
            if res == target:
                return [p1+1,p2+1]
            elif res > target:
                p2 -= 1
            elif res < target:
                p1 += 1
        return [0]