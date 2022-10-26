class UnionFind:
    def __init__(self, n = 0):
        self.parent = [x for x in range(n)]
    
    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y: return False
        self.parent[y] = x
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.n = n
        self.edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        self.edges.sort(key = lambda x : x[2])
        
        base = self.exclude_edge(-1)
        critical, pseudoCritical = set(), set()
        for i in range(len(edges)):
            if self.exclude_edge(i) > base:
                critical.add(self.edges[i][3])
            else:
                if self.include_edge(i) == base:
                    pseudoCritical.add(self.edges[i][3])
                    
        return [list(critical), list(pseudoCritical)]
           
                         
    def include_edge(self, include):
        uf = UnionFind(self.n)
        u0, v0, w0, _ = self.edges[include]
        ans = w0
        uf.union(u0, v0)
            
        for i, (u, v, w, _) in enumerate(self.edges):
            if uf.union(u, v): ans += w
            
        p = uf.find(0)
        for node in range(self.n):
            if uf.find(node) != p: 
                return math.inf
        
        return ans
    
    def exclude_edge(self, exclude):
        uf = UnionFind(self.n)
        ans = 0
        for i, (u, v, w, _) in enumerate(self.edges):
            if i == exclude: continue
            if uf.union(u, v): ans += w
        
        p = uf.find(0)
        for node in range(self.n):
            if uf.find(node) != p: 
                return math.inf
        
        return ans
        