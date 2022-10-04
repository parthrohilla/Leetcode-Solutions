class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a*a <= c:
            temp = c - a*a
            if temp == math.isqrt(temp) ** 2: return True
            a += 1
        return False