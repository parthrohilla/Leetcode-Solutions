class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        # Make adjacency List in the form {A : [B, W]}
        # Here adjacency list represents a map that represents and edge from A to B with W weight 
        for edge,probablity in zip(edges, succProb):
            a, b = edge[0], edge[1]
            # -1 multiplied as we would be using a min-heap functioning as a max-heap since we are required to return the max-probabilty
            adj[a].append((b,-1*probablity))
            adj[b].append((a,-1*probablity))    
            
        # Use of a min-Heap for Dijkstra's Algorithm    
        heap = [(-1,start)]
        visited = {}
        while heap:
            prob,node = heapq.heappop(heap)
            visited[node] = prob
            if node == end: #Return Probability when we reach the destination Node
                return -1 * prob
            for nei,weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (-1*prob*weight,nei))
        # Return Zero when we were never able to reach the destination node            
        return 0
                    
            
        
        