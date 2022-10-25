class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [x for x in range(n+1)]
        indegrees = [-1]*(n+1)
        
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return True
            parent[y] = x
            return False
        
        bl1 = bl2 = -1
        for i, (u,v) in enumerate(edges):
            if indegrees[v] == -1:
                indegrees[v] = i
            else:
                bl1 = i
                bl2 = indegrees[v]
        
        for i, (u,v) in enumerate(edges):
            if i == bl1: continue
            if union(u,v):
                if bl1 == -1: return edges[i]
                else: return edges[bl2]
                
        return edges[bl1]
                
            
        
        
        