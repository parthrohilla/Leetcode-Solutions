class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        
        def dfs(i):
            visited.add(i)
            for u in adj[i]:
                if u not in visited:
                    dfs(u)
        
        
        count, visited = 0, set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count