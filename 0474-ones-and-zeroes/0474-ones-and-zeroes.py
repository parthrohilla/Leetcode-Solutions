class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros_ones = [[s.count("0"), s.count("1")] for s in strs]
        
        @lru_cache(None)
        def dfs(index, ones, zeros):
            if index >= len(strs): return 0
            
            pick = -1
            Z, O = zeros_ones[index]
            
            ignore = dfs(index + 1, ones, zeros)
            if ones + O <= n and zeros + Z <= m:
                pick = 1 + dfs(index + 1, ones + O, zeros + Z)
                
            return max(pick, ignore)
        
        return dfs(0,0,0)