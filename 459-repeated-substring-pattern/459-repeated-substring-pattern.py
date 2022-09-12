class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            if s == s[0:i+1]*(n//(i+1)): return True
        return False
        