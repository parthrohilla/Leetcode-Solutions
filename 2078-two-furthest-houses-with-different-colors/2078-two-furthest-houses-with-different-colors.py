class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        self.ans = 0
        
        for i,c in enumerate(colors):
            if c != colors[-1]: self.ans = max(self.ans, len(colors) - i - 1)
            if c != colors[0]: self.ans = max(self.ans, i)
        
        return self.ans
    