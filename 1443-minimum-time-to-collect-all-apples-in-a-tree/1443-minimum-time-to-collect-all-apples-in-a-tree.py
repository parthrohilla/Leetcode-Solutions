class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
            
        self.cost = 0
        def dfs(node, parent):
            found = False
            for child in G[node]:
                if child != parent and dfs(child, node):
                    found = True
                    self.cost += 2
            return found or hasApple[node]
        
        dfs(0,-1)
        return self.cost