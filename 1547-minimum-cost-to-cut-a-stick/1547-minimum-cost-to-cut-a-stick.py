class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i>j: return 0
            
            mini = math.inf
            for k in range(i,j+1,1):
                mini = min(mini, cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j))
            return mini
        
        c = len(cuts)
        cuts.sort()
        cuts = [0] + cuts + [n]
        print(len(cuts))
        return dfs(1,c)