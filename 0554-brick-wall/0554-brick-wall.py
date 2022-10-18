class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        corner, rows = {}, len(wall)
        for i in range(rows):
            prefix = 0
            for k in wall[i][:-1]:
                prefix += k
                corner[prefix] = 1 + corner.get(prefix, 0)
        
        max_brick_edges = max(corner.values()) if corner else 0
        return rows - max_brick_edges