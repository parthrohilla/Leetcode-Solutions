class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, amount) -> int:
            if amount == 0:
                return 0
            if i>=len(coins) or amount < 0:
                return math.inf
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            memo[(i, amount)] = min(1 + dfs(i, amount-coins[i]), dfs(i+1, amount))
            return memo[(i, amount)]
        
        temp = dfs(0, amount)
        return temp if temp != math.inf else -1