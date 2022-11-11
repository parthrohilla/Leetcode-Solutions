class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        N = n
        base = 1
        def helper(num):
            return sum(map(int,list(str(num))))
        
        while helper(N) > target:
            N = (N // 10 + 1)
            base *= 10
        
        return N * base - n