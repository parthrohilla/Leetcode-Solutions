class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
            
        self.cost = 0
        visited = set()
        def dfs(node):
            if node in visited: return False
            visited.add(node)
            found = False
            for nei in G[node]:
                if dfs(nei):
                    found = True
                    self.cost += 2
            return found or hasApple[node]
        
        dfs(0)
        return self.cost