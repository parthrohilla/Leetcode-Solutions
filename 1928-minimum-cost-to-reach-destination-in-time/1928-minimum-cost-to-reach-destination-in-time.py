class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        adj = defaultdict(list)
        for u,v,t in edges:
            adj[u].append([v, t])
            adj[v].append([u, t])
        
        heap = [[0, passingFees[0], 0]]
        cost = [-1]*len(passingFees)
        while heap:
            t, currentcost, node = heapq.heappop(heap)
            if cost[node] < 0 or currentcost < cost[node]:
                cost[node] = currentcost
                for nei, tt in adj[node]:
                    if t + tt <= maxTime:
                        heapq.heappush(heap, [t + tt, currentcost + passingFees[nei], nei])
        
        return cost[len(passingFees)-1]