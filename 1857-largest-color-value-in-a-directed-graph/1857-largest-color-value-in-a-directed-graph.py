class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, adj, visited, dfs_visited = len(colors), defaultdict(list),set(), set()
        for a,b in edges: adj[a].append(b)
        
        def dfs_cycle(i):
            visited.add(i)
            dfs_visited.add(i)
            for nei in adj[i]:
                if nei in visited and nei in dfs_visited: return True
                if nei not in visited and dfs_cycle(nei): return True
            dfs_visited.remove(i)
            return False
        
        for i in range(n):
            if i not in visited and dfs_cycle(i): return -1
        
        @lru_cache(None)
        def dfs(i, color):
            count = 0
            if color == colors[i]:
                count += 1
            
            mx = 0
            for nei in adj[i]:
                mx = max(mx,dfs(nei,color))
            return mx + count

        res = 0
        for i in range(n):
            res = max(res, dfs(i,colors[i]))
        return res
        
        
        
        
        
        
    
        