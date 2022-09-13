class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return 0.5*max(([ abs( ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)) for (ax,ay),(bx,by),(cx,cy) in itertools.combinations(points,3)]))