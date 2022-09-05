class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for xc, yc, r in queries:
            count = 0
            for i,j in points:
                if (i-xc)**2 + (j-yc)**2 - r**2 <= 0:
                    count += 1
            ans.append(count)
        return ans
            