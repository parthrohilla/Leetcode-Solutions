class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lookup = {}
        def dfs(s1, s2):
            if not s1 or not s2: return 0
            if (s1,s2) in lookup: return lookup[(s1,s2)]
            
            if s1[0] == s2[0]:
                lookup[(s1,s2)] = 1 + dfs(s1[1:], s2[1:])
            else:
                lookup[(s1,s2)] = max(dfs(s1,s2[1:]), dfs(s1[1:], s2))
            return lookup[(s1,s2)]
        
        return dfs(text1, text2)