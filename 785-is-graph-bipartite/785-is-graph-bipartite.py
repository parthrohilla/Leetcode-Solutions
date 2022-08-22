class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        visited = [0 for _ in range(len(graph))]
        
        def dfs(node, colour):
            if visited[node]:
                return visited[node] == colour
            
            visited[node] = colour
            for n in graph[node]:
                if not dfs(n, -1 * colour):
                    return False
            return True
            
        
        for node in range(len(graph)):
            if visited[node] == 0 and not dfs(node, 1):
                return False
        
        return True