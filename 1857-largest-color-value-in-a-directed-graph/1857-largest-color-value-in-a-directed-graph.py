class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, adj, visited, dfs_visited = len(colors), defaultdict(list),set(), set()
        for a,b in edges: adj[a].append(b)
        # Return -1 if it's a cycliv graph
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
        
        # Calculate color path from each node
        memo = {}
        def dfs(i, color):
            if (i,color) in memo: 
                return memo[(i,color)]
            
            count = 0
            if color == colors[i]: 
                count += 1
            mx = 0
            for nei in adj[i]:
                mx = max(mx,dfs(nei,color))
            
            memo[(i,color)] = mx + count
            return memo[(i,color)]

        res = 0
        for i in range(n):
            res = max(res, dfs(i,colors[i]))
        return res
        
        
        
        
        
        
    
        