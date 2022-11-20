class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        G = defaultdict(list)
        for u,v in roads:
            G[u].append(v)
            G[v].append(u)
        
        def dfs(u,parent):
            passengers = 1
            for v in G[u]:
                if v != parent:
                    small = dfs(v,u)
                    self.cost += (small + seats - 1) // seats
                    passengers += small
            return passengers
                    
        self.cost = 0
        dfs(0,-1)
        return self.cost
        