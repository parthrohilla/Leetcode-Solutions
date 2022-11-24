class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i,house in enumerate(colors):
            if house != colors[-1]: ans = max(ans, len(colors) - i - 1)
            if house != colors[0]: ans = max(ans, i)
        return ans
    