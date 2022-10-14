class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left = max(A,E)
        right = max(min(C,G), left)
        bottom = max(B,F)
        top = max(min(D,H), bottom)
        return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F);