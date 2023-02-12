class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        buffer = ""
        for i in range(len(digits)):
            buffer += str(digits[i])
        buffer = int(buffer)
        buffer += 1 
        buffer = str(buffer)
        for i in range(len(buffer)):
            res.append(int(buffer[i]))
        return res