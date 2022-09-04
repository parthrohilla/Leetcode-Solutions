class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b,time in roads:
            adj[a].append((b,time))
            adj[b].append((a,time))
        
        times, ways = [math.inf]*n,  [math.inf]*n
        times[0], ways[0] = 0, 1
        heap = [(0,0)]
        while heap:
            time,node = heapq.heappop(heap)
            
            for b,t in adj[node]:
                if time + t < times[b]:
                    times[b] = time + t
                    ways[b] = ways[node]
                    heapq.heappush(heap,(time+t,b))
                elif time + t == times[b]:
                    ways[b] += ways[node]
        return ways[-1]%(10**9 + 7)