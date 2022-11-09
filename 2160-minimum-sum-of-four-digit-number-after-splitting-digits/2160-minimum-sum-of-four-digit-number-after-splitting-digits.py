class Solution:
    def minimumSum(self, num: int) -> int:
        N = sorted(str(num))
        return int(N[0] + N[3]) + int(N[1] + N[2])
        
                
        