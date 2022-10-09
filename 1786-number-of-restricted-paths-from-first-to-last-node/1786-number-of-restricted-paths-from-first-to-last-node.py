class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        d, visited, adj, mod = [math.inf]*n, set(), defaultdict(list), (10**9) + 7
        # Creaste Adjacency List
        for u,v,w in edges:
            adj[u-1].append([v-1,w])
            adj[v-1].append([u-1,w])
        # Djisktra's Algorith for shortest path
        heap = [[0,n-1]]
        while heap:
            distance, node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                d[node] = distance

                for nei, weight in adj[node]:
                    if nei not in visited:
                        heapq.heappush(heap,[distance+weight, nei])
                        
        # DFS for finding the increasing distance path, can be seen as LIS on a Graph
        @lru_cache(None)
        def dfs(i):
            if i == 0: return 1
            count = 0
            for nei, wei in adj[i]:
                if nei not in path:
                    if d[nei] > d[i]:
                        count =(count + dfs(nei)) % mod
            return count
        
        return dfs(n-1)