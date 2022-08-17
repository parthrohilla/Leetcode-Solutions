class Solution:
    def minOperations(self, s: str) -> int:
        res = sum([1 for i,char in enumerate(s) if i%2 != int(char)])
        return min(res, len(s)-res)