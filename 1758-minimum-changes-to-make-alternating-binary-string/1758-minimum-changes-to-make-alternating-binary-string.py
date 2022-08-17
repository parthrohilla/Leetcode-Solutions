class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            if int(s[i]) != i % 2:
                count += 1
        return min(count, n-count)