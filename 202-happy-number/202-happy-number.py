class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            n = self.sumOfSquares(n)
            if n in seen:
                return False
            else:
                seen.add(n)
    
    def sumOfSquares(self, n):
        ans = 0
        while n:
            rem = n % 10
            ans += rem**2
            n = n // 10
        return ans