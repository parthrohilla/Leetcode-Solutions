class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = [[] for _ in range(n)]
        
        # make adjacency list
        for a,b in prerequisites:
            adj[b].append(a)
        
        visited, dfs_visited = [False] * n, [False] * n
        for i in range(n):
            if not visited[i]:
                if self.cycle_present(i, adj, visited, dfs_visited):
                    return []
        
        
        ans = []
        visited = [False for _ in visited]
        def dfs(i):
            visited[i] = True
            for u in adj[i]:
                if not visited[u]:
                    dfs(u)
            ans.append(i)
        
        def topological_sort():
            for i in range(n):
                if not visited[i]:
                    dfs(i)
        
        topological_sort()
        return ans[::-1]

    
    def cycle_present(self, i, adj, visited, dfs_visited):
        visited[i] = True
        dfs_visited[i] = True
        
        for u in adj[i]:
            if visited[u] and dfs_visited[u]:
                return True
            elif not visited[u]:
                if self.cycle_present(u, adj, visited, dfs_visited):
                    return True
            
        dfs_visited[i] = False
        return False
        
            