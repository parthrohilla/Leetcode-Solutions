class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[b].append(a)
        
        def dfs(node):
            res = []
            
            if node in memo: 
                return memo[node]
            
            for nei in adj[node]:
                res += [nei] + dfs(nei)
            
            memo[node] = sorted(list(set(res)))
            return memo[node]
            
        memo = {}
        ans = [[] for _ in range(n)]
        k = adj.keys()
        for i in range(n):
            if i in adj:
                ans[i] = dfs(i)
        
        return ans