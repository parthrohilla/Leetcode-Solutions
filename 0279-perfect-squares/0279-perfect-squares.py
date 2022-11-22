class Solution:
    memo = {}
    def numSquares(self, n: int) -> int:
        return self.helper(n)
        
    def helper(self, n:int)->int:
        if n in self.memo:
            return self.memo[n]
        
        if n==0:
            return 0
        
        output = 100000
        for i in range(1, floor(sqrt(n))+1):
            small = self.helper(n-i*i)
            output = min(output, small+1)
        
        self.memo[n] = output
        return output