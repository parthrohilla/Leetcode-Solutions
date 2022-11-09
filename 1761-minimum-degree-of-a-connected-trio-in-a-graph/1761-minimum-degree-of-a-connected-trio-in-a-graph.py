class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        deg = [0]*n # For Storing Degrees of nodes
        G = [[False]*n for _ in range(n)] # Adjacency Matrix as we need to check connectivity between any 2 nodes in O(1)
        
        # Filling degree list and connectivity Matrix for faster lookup
        for u,v in edges:
            u, v = u-1, v-1
            G[u][v] = G[v][u] = True
            deg[u] += 1
            deg[v] += 1
    
        # Try for all combinations of 3 Nodes and check if they form a trio 
        # i.e. for any 3 nodes i, j, k in trio G[i][j] = G[j][k] = G[i][k] = True
        ans = math.inf
        for i in range(n):
            for j in range(i+1,n):
                if G[i][j]:
                    for k in range(j+1,n):
                        if G[i][k] and G[j][k]:
                            ans = min(ans, deg[i] + deg[j] + deg[k] - 6)
        
        return ans if ans < math.inf else -1
        