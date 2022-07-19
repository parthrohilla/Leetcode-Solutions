class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, memo = len(prices), {}
        
        def dfs(i, canbuy):
            if i >= n:
                return 0
            if (i, canbuy) in memo:
                return memo[(i, canbuy)]
            
            profit = 0
            if canbuy:
                profit = max(-prices[i] + dfs(i+1, False), dfs(i+1, True))
            else:
                profit = max(prices[i] + dfs(i+2, True), dfs(i+1, False))
            memo[(i, canbuy)] = profit
            return profit
        
        return dfs(0, True)