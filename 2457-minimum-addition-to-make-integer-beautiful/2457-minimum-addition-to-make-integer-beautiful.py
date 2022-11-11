class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        N = n
        base = 1
        SUM_of_DIGITS = lambda num : sum(map(int,str(num)))
        
        while SUM_of_DIGITS(N) > target:
            N = (N // 10 + 1)
            base *= 10
        
        return N * base - n