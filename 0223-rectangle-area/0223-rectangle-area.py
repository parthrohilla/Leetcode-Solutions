class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        left, bottom = max(A,E), max(B,F)
        right, top = max(min(C,G), left), max(min(D,H), bottom)
        
        rect1 = (C-A)*(D-B)
        rect2 = (G-E)*(H-F)
        common_rect = (right-left)*(top-bottom)
        return rect1 + rect2 - common_rect