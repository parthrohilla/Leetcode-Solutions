class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n, memo = len(prices), {}
        
        def dfs(i, canbuy, transactions):
            if i == n or transactions == k:
                return 0
            if (i, canbuy, transactions) in memo:
                return memo[(i, canbuy, transactions)]
            
            profit = 0
            if canbuy:
                profit = max(-prices[i] + dfs(i+1, False, transactions), dfs(i+1, True, transactions))
            else:
                profit = max(prices[i] + dfs(i+1, True, transactions+1), dfs(i+1, False, transactions))
            memo[(i, canbuy, transactions)] = profit
            return profit
        
        return dfs(0, True, 0)