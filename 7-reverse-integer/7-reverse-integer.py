class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        ans = 0
        while temp:
            rem = temp % 10
            temp = temp // 10
            ans = ans*10 + rem
        
        if ans < -2**31 or ans > 2**31-1:
            return 0
        elif x < 0:
            return -ans
        else:
            return ans