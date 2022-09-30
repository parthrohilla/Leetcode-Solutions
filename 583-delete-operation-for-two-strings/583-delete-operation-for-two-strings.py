class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        lookup = {}
        def dfs(i,j):
            if i == m or j == n: return max(m-i,n-j)
            if (i,j) in lookup: return lookup[(i,j)]
            if word1[i] == word2[j]: 
                lookup[(i,j)] = dfs(i+1, j+1)
            else:
                lookup[(i,j)] = 1 + min(dfs(i+1,j), dfs(i,j+1))
            return lookup[(i,j)]
        return dfs(0,0)