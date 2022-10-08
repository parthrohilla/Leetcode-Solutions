class Solution:
    def checkPartitioning(self, s: str) -> bool:
        memo = {}
        def dfs(substring, partitions):
            if partitions == 0: return substring == substring[::-1]
            if (substring, partitions) in memo: return memo[(substring, partitions)]
            
            ans = False
            for i in range(1,len(substring)):
                if substring[:i] == substring[:i][::-1] and dfs(substring[i:], partitions - 1): 
                    ans= True
            memo[(substring, partitions)] = ans
            return ans
        return dfs(s,2)
    
