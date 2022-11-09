class Solution:
    def maximumScore(self, values: List[int], edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for u,v in edges:
            G[u].append([values[v],v])
            G[v].append([values[u],u])
            
        for i in range(len(values)):
            G[i].sort(reverse = True)
            G[i] = G[i][:3]
        
        ans = -1
        for u,v in edges:
            for neiU, i in G[u]:
                for neiV, j in G[v]:
                    if i != v and j != u and i != j:
                        ans = max(ans, values[u] + values[v] + neiU + neiV)
                        
        return ans
            