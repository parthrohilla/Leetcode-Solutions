class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for eq,val in zip(equations, values):
            i,j = eq[0], eq[1]
            adj[i][j] = val
            adj[j][i] = 1/val
        
        def dfs(curr,end,value):
            if curr not in adj or end not in adj: return -1
            if end == curr: return value
            
            visited.add(curr)
            for nei,v in adj[curr].items():
                if nei not in visited:
                    res = dfs(nei, end, value*v)
                    if res != -1:
                        return res
            visited.remove(curr)
            return -1
            
        ans = []
        visited = set()
        for a,b in queries:
            ans.append(dfs(a,b,1))
            visited.clear()
        return ans