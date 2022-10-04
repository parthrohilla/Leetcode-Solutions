class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        ans = ""
        negative = True if num<0 else False
        num = abs(num)
        while num:
            rem = num % 7
            ans = str(rem) + ans
            num = num // 7
        return "-"+ans if negative else ans