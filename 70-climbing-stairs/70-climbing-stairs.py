class Solution:
    def climbStairs(self, n: int) -> int:
        memo= {}
        
        def helper(steps)->int:
            if steps == 1:
                return 1
            if steps == 2:
                return 2
            if steps in memo:
                return memo[steps]
            
            small1 = helper(steps-1)
            small2 = helper(steps-2)
            memo[steps] = small1 + small2
            return memo[steps]
        
        return helper(n)
            