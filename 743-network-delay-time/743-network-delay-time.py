class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
            
        heap = [(0,k)] #(time, node)
        visited = set()
        t = 0
        while heap:
            weight, node = heapq.heappop(heap)
            visited.add(node)
            if len(visited) == n:
                return weight
            for nei, w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (weight + w,nei))
            
        return -1
            