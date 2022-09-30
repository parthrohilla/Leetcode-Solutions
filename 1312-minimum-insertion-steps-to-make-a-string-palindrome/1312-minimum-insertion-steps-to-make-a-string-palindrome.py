class Solution:
    def minInsertions(self, s: str) -> int:
        def dfs(i,j):
            if i >= j: return 0
            if (i,j) in lookup: return lookup[(i,j)]
            
            if s[i] == s[j]: lookup[(i,j)] = dfs(i+1, j-1)
            else: lookup[(i,j)] = 1 + min(dfs(i+1,j), dfs(i,j-1))
            return lookup[(i,j)]
        lookup = {}
        return dfs(0,len(s)-1)