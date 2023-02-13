
#one line code
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
#optimized code but its python so memory management is sh#t
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max = 0
        index = -1
        for i in range(len(arr)-1):
            if arr[i] > max:
                max = arr[i]
                index = i

        return index