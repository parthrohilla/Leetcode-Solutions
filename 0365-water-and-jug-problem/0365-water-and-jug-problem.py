class Solution:
    def canMeasureWater(self, a: int, b: int, c: int) -> bool:
        if c > a + b: return False
        if c == a or c == b: return True
        return c % gcd(a,b) == 0