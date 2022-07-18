class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        memo = [ [-1 for _ in range(target+1)] for _ in range(len(coins)) ]
        
        def dfs(i, current) ->int:
            if current == target:
                return 1
            if i == len(coins) or current > target:
                return 0
            if memo[i][current] != -1:
                return memo[i][current]
            
            op1 = dfs(i, current + coins[i])
            op2 = dfs(i+1, current)
            memo[i][current] = op1 + op2
            return memo[i][current]
        
        return dfs(0, 0)