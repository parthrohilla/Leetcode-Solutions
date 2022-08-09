class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        
        #create adj list
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        heap = [[0,0]]
        heapq.heapify(heap)
        visited = set()
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for d,j in adj[i]:
                if j not in visited:
                    heapq.heappush(heap, [d,j])
        
        return res