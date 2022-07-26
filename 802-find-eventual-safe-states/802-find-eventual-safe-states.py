class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited, dfs_visited = [False]*n, [False]*n
        cycle = [False]*n
        
        def dfs(vertex):
            visited[vertex] = True
            dfs_visited[vertex] = True
            
            for u in graph[vertex]:
                if not visited[u]:
                    if dfs(u):
                        cycle[vertex] = True
                        return True
                elif visited[u] and dfs_visited[u]:
                    cycle[vertex] = True
                    return True
            
            dfs_visited[vertex] = False
            return False
            
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return [i for i,x in enumerate(cycle) if x == False]
        