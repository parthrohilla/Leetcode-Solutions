class Solution:
    def isUgly(self, n: int) -> bool:
        for x in [2,3,5]:
            while  n > 1 and n % x == 0:
                n //= x
        return n == 1