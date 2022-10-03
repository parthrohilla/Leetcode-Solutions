class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key = lambda x: len(x))
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if self.isChain(words[i],words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
    
    def isChain(self, s1, s2):
        if len(s1) - len(s2) != 1: return False
        for i in range(len(s1)):
            if s1[:i] + s1[i+1:] == s2: return True
        return False