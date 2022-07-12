class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x, n // 2)
            res = res * res
            return res * x if n % 2 == 1 else res
        
        if n < 0:
            return (1 / helper(x, abs(n)))
        else:
            return helper(x, n)