class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if (i, j) in memo:
                return memo[(i, j)]
            
            ans = math.inf
            if word1[i] == word2[j]:
                ans = min(ans, dfs(i-1, j-1))
            else:
                insert = 1 + dfs(i, j-1)
                delete = 1 + dfs(i-1, j)
                replace = 1 + dfs(i-1, j-1)
                ans = min(ans, insert, delete, replace)
            memo[(i, j)] = ans
            return ans
        
        
        return dfs(len(word1)-1, len(word2)-1)