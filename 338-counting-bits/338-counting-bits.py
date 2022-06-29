class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        while n:
            output.append(self.countOnes(n))
            n -= 1
        output.append(0)
        return output[::-1]
    
    def countOnes(self, n) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count