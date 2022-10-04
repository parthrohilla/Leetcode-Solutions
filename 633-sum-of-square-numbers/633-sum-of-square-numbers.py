class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a*a <= c:
            b_square = c - a*a
            if b_square == math.isqrt(b_square) ** 2: return True
            a += 1
        return False