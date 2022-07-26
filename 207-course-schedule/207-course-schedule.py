class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        
        # Make an adjacency list
        for a,b in prerequisites:
            adj[a].append(b)
            
        def dfs(vertex):
            visited[vertex] = True
            dfs_visited[vertex] = True
            
            for u in adj[vertex]:
                if visited[u] and dfs_visited[u]:
                    return True
                elif not visited[u]:
                    if dfs(u):
                        return True
            
            dfs_visited[vertex] = False
            return False
        
        visited, dfs_visited = [False]*numCourses, [False]*numCourses
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
                
        return True