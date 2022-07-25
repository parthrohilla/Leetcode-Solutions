class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * n
        q = deque()
        q.append(source)
        visited[source] = True
        while q:
            u = q.popleft()
            for vertex in adj_list[u]:
                if visited[vertex] == False:
                    q.append(vertex)
                    visited[vertex] = True
        
        return visited[destination]