class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        C = Counter(text)
        ans = 0
        
        def possible():
            if C["b"] >= 1 and C["a"] >= 1 and C["l"] >= 2 and C["o"] >= 2 and C["n"] >= 1: return True
            return False
        
        while possible():
            ans += 1
            C["b"] -= 1
            C["a"] -= 1
            C["l"] -= 2
            C["o"] -= 2
            C["n"] -= 1
        
        return ans