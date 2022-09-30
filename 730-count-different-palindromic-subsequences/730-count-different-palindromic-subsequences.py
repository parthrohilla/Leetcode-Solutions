class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        memo = {}
        def dfs(i,j):
            if i > j: return 0
            if i == j: return 1
            if (i,j) in memo: return memo[(i,j)]
            count = 0
            if s[i] == s[j]:
                count = 2*dfs(i+1,j-1)
                left, right = i+1, j-1
                while left <= right and s[i] != s[left]: left += 1
                while right >= left and s[i] != s[right]: right -= 1
                
                if left < right: count -= dfs(left+1, right-1)
                elif left == right: count += 1
                else: count += 2
            else:
                count = dfs(i+1,j) + dfs(i,j-1) - dfs(i+1,j-1) 
            memo[(i,j)] =  count % 1000000007
            return memo[(i,j)]
        
        return dfs(0,len(s)-1)