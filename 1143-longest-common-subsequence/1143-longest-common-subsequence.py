class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(s1, s2):
            if not s1 or not s2:
                return 0
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            ans = 0
            if s1[0] == s2[0]:
                ans = 1 + dfs(s1[1:], s2[1:])
            else:
                ans = max(dfs(s1, s2[1:]), dfs(s1[1:], s2))
            memo[(s1, s2)] = ans
            return ans
        
        return dfs(text1, text2)