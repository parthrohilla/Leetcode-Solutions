class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        S = sorted([a,b,c])
        
        if S[2] > S[0] + S[1]: return S[0] + S[1]
        return sum(S)//2