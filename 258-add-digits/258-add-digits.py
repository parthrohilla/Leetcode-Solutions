class Solution:
    def addDigits(self, n: int) -> int:
        while n // 10:
            n = self.sum_of_digits(n)
        return n

    def sum_of_digits(self, n):
        ans = 0
        while n:
            rem = n % 10
            ans += rem
            n = n // 10
        return ans