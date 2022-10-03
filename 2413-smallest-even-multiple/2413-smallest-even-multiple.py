class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        hcf = 2 if n % 2 == 0 else 1
        return (2*n)//hcf
        