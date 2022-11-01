class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = []
        points = set([x[0] for x in buildings] + [x[1] for x in buildings])
        ans = [[-1, 0]]
        
        def addToSkyline(P):
            if ans[-1][1] != P[1]:
                ans.append(P)
        
        i = 0
        for p in sorted(points):
            
            while i < len(buildings) and buildings[i][0] <= p:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            
            while heap and heap[0][1] <= p:
                heapq.heappop(heap)
                
            height = -heap[0][0] if heap else 0
            addToSkyline((p, height))
        
        return ans[1:]