class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i,c in enumerate(colors):
            if c != colors[-1]: ans = max(ans, len(colors) - i - 1)
            if c != colors[0]: ans = max(ans, i)
        return ans
    