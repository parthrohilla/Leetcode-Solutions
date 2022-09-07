class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        steps = 0
        for i in range(n-1):
            a,b = points[i]
            c,d = points[i+1]
            steps += max(abs(a-c), abs(b-d))
        return steps