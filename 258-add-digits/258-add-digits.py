class Solution:
    def addDigits(self, n: int) -> int:
        if n == 0:
            return 0
        elif n % 9 == 0:
            return 9
        else:
            return n % 9