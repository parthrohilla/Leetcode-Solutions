class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [[s.count("0"), s.count("1")] for s in strs]
        
        @lru_cache(None)
        def dfs(index, ones, zeros):
            if index >= len(strs): return 0
            pick = -1
            ignore = dfs(index + 1, ones, zeros)
            z,o = xy[index]
            if ones + o <= n and zeros + z <= m:
                pick = 1 + dfs(index + 1, ones + o, zeros + z)
            return max(pick, ignore)
        return dfs(0,0,0)