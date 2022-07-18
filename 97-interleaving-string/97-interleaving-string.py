class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        def dfs(i, j, k):
            if k == len(s3):
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            ans = False
            if i < len(s1) and j <len(s2) and s3[k] == s1[i] == s2[j]:
                ans = dfs(i+1, j, k+1) or dfs(i, j+1, k+1)
            elif i < len(s1) and s1[i] == s3[k]:
                ans = dfs(i+1, j, k+1)
            elif j < len(s2) and s2[j] == s3[k]:
                ans = dfs(i, j+1, k+1)
                
            memo[(i,j,k)] = ans
            return ans
        
        return dfs(0,0,0)
                
            