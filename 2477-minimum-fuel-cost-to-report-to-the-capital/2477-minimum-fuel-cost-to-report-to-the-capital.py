class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        G = defaultdict(list)
        for u,v in roads:
            G[u].append(v)
            G[v].append(u)
        
        def dfs(u,parent):
            total_passengers = 1
            for v in G[u]:
                if v != parent:
                    passengers = dfs(v,u)
                    self.cost += (passengers + seats - 1) // seats
                    total_passengers += passengers
            return total_passengers
                    
        self.cost = 0
        dfs(0,-1)
        return self.cost
        