class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(index, ones, zeros):
            if index == len(strs): return 0
            
            C = Counter(strs[index])
            pick, ignore = -1, -1
            
            if ones + C["1"] <= n and zeros + C["0"] <= m:
                pick = 1 + dfs(index + 1, ones + C["1"], zeros + C["0"])
            ignore = dfs(index + 1, ones, zeros)
            
            return max(pick, ignore)
        
        return dfs(0,0,0)