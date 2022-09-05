class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        #dfs helper
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited and nei not in restricted:
                    dfs(nei)
        
        visited = set()
        dfs(0)
        return len(visited)
        