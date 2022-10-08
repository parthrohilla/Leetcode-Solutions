class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @lru_cache(None)
        def dfs(substring, partitions):
            if partitions == 0: return substring == substring[::-1]
            for i in range(1,len(substring)):
                if substring[:i] == substring[:i][::-1] and dfs(substring[i:], partitions - 1):
                    return True
        return dfs(s,2)
    
