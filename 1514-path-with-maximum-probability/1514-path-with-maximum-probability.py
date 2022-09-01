class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        # Make adjacency List
        for edge,probablity in zip(edges, succProb):
            a, b = edge[0], edge[1]
            adj[a].append((b,-1*probablity))
            adj[b].append((a,-1*probablity))
            
        heap = [(-1,start)]
        visited = {}
        while heap:
            prob,node = heapq.heappop(heap)
            
            visited[node] = prob
            if node == end:
                return -1 * prob
            
            for nei,weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (-1*prob*weight,nei))
        return 0
                    
            
        
        