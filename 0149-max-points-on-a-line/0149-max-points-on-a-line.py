class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        def find_slope(p1, p2):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            return (y2-y1)/(x2-x1)if x2 != x1 else math.inf

        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for p2 in points[i+1:]:
                m = find_slope(p1, p2)
                slopes[m] += 1
                ans = max(ans, slopes[m])
        
        return ans+1