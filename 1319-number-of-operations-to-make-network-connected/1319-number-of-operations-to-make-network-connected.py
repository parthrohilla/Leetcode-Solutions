class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if n-1 > len(connections):
            return -1
        
        adj = defaultdict(list)
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            seen.add(node)
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei)
        
        components = 0
        seen = set()
        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1
        
        #Final Return condition
        return components-1
        