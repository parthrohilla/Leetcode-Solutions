class Solution:
    def minimumSum(self, num: int) -> int:
        N = sorted(str(num))
        n1 = N[0] + N[3]
        n2 = N[1] + N[2]
        return int(n1) + int(n2)
        
                
        