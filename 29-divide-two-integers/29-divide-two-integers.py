class Solution:
    def divide(self, a: int, b: int) -> int:
        return min(2**31 - 1, max(int(a/b), -2**31))