class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        deg = [0]*n
        G = [[False]*n for _ in range(n)]
        
        for u,v in edges:
            u, v = u-1, v-1
            deg[u] += 1
            deg[v] += 1
            G[u][v] = True
            G[v][u] = True
            
        ans = math.inf
        for i in range(n):
            for j in range(i+1,n):
                if G[i][j]:
                    for k in range(j+1,n):
                        if G[i][k] and G[j][k]:
                            ans = min(ans, deg[i] + deg[j] + deg[k] - 6)
        
        return ans if ans < math.inf else -1
        