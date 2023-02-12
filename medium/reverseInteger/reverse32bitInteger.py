class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
        x = str(abs(x))
        x = x[::-1]
        res = None
        if isNegative:
            res =  int(x) * -1
        else:
            res =  int(x)

        if res not in range(-2**31,(2**31)-1):
            return 0
        return res