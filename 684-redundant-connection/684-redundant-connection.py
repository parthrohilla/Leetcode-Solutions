class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def path(start, end, parent):
            if start == end:
                return True
            
            for nei in adj[start]:
                if nei != parent and path(nei, end, start):
                    return True
            return False
        
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        
        for a, b in edges:
            # If the path already exists then return this edge
            if path(a,b, 0):
                return [a,b]
            else:
                adj[a].append(b)
                adj[b].append(a)
        