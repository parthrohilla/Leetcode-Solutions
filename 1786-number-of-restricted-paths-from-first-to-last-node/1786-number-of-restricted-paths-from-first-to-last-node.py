class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        d = [math.inf]*n
        visited = set()
        heap = [[0,n-1]]
        adj = defaultdict(list)
        
        for u,v,w in edges:
            adj[u-1].append([v-1,w])
            adj[v-1].append([u-1,w])
        
        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            visited.add(node)
            d[node] = distance
            
            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,[distance+weight, nei])
        
        mod = (10**9) + 7
        visited = set()
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 1
            visited.add(i)
            count = 0
            for nei, wei in adj[i]:
                if nei not in visited:
                    if d[nei] > d[i]:
                        count += dfs(nei) % mod
            visited.remove(i)
            return count % mod
        
        return dfs(n-1)