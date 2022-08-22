class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        visited = [-1 for _ in range(len(graph))]
        
        for node in range(len(graph)):
            if visited[node] == -1:
                q.append((node, 0))
                visited[node] = 0
                
                while q:
                    node, colour = q.popleft()
                    for n in graph[node]:
                        if visited[n] == -1:
                            q.append((n,colour ^ 1))
                            visited[n] = colour ^ 1
                        elif visited[n] == colour:
                            return False
        
        return True