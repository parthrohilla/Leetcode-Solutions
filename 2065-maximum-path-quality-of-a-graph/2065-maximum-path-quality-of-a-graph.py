class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        G = defaultdict(list)
        for u,v,w in edges:
            G[u].append([v,w])
            G[v].append([u,w])
            
        def dfs(current, path, left):
            if current == 0:
                tmp = 0
                for node in path:
                    tmp += values[node]
                self.best = max(self.best, tmp)
            
            for nei, wei in G[current]:
                if wei <= left:
                    dfs(nei, {nei} | path, left - wei)
        
        self.best = 0
        dfs(0, {0}, maxTime)
        return self.best