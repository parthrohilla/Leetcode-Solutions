class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[False]*n for _ in range(n)]
        for u,v in prerequisites:
            adj[u][v] = True
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] |= adj[i][k] and adj[k][j]
        
        ans = []
        for u,v in queries:
            ans.append(adj[u][v])
        return ans
    