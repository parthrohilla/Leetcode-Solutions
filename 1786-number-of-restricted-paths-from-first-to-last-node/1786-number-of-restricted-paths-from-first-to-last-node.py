class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        d, visited, adj, mod = [math.inf]*n, set(), defaultdict(list), (10**9) + 7
        for u,v,w in edges:
            adj[u-1].append([v-1,w])
            adj[v-1].append([u-1,w])
        
        heap = [[0,n-1]]
        while heap:
            distance, node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                d[node] = distance

                for nei, weight in adj[node]:
                    if nei not in visited:
                        heapq.heappush(heap,[distance+weight, nei])
                        
        path = set()
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 1
            path.add(i)
            
            count = 0
            for nei, wei in adj[i]:
                if nei not in path:
                    if d[nei] > d[i]:
                        count += dfs(nei) % mod
            
            path.remove(i)
            return count % mod
        
        return dfs(n-1)