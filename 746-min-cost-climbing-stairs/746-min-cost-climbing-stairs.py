class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def helper(i):
            if i == n-1 or i == n-2:
                return cost[i]
            if i in memo:
                return memo[i]
            
            small1 = cost[i] + helper(i+1)
            small2 = cost[i] + helper(i+2)
            memo[i] = min(small1, small2)
            return memo[i]
        
        return min(helper(0), helper(1))
            