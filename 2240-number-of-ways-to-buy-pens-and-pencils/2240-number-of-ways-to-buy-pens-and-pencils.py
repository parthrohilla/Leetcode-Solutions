class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        A = 0
        B = (total - A*cost1) // cost2
        while B >= 0:
            ways += (B+1)
            A += 1
            
            B = (total - A*cost1) // cost2
            
        return ways