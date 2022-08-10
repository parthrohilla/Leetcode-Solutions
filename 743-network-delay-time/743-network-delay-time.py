class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])
        
        heap = [[0, k]]
        t = 0
        visited = set()
        while heap:
            u,v = heapq.heappop(heap)
            if v in visited:
                continue
            
            visited.add(v)
            t = max(t, u)
            for u2, v2 in adj[v]:
                if u2 not in visited:
                    heapq.heappush(heap, [u+v2, u2])
        return t if len(visited) == n else -1