class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def dfs(i,j):
            if i>j: return 0
            if (i,j) in memo: return memo[(i,j)]
            
            mini = math.inf
            for k in range(i,j+1,1):
                mini = min(mini, cuts[j+1] - cuts[i-1] + dfs(i,k-1) + dfs(k+1,j))
            memo[(i,j)] = mini
            return mini
        
        cuts.sort()
        cuts = [0] + cuts + [n]
        return dfs(1,len(cuts)-2)