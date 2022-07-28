class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(start, end, parent):
            if start == end:
                return True
            
            for v in adj[start]:
                if v != parent:
                    if dfs(v, end, start):
                        return True
            return False
        
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        
        for start, end in edges:
            if dfs(start, end, 0):
                return [start,end]
            else:
                adj[start].append(end)
                adj[end].append(start)