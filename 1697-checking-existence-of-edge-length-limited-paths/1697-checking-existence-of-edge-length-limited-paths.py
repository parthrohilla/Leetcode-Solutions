class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
    
    def find(self, x):
        if x == self.parent[x]: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y: return
        self.parent[y] = x

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = [(u, v, limit, index) for index, (u, v, limit) in enumerate(queries)]
        queries.sort(key = lambda x: x[2])
        edgeList.sort(key = lambda x: x[2])
        
        edgeList = deque(edgeList)
        ans = [None] * len(queries)
        
        dsu = DSU(n)
        for u, v, limit, i in queries:
            while edgeList and edgeList[0][2] < limit:
                dsu.union(edgeList[0][0], edgeList[0][1])
                edgeList.popleft()
            
            ans[i] = (dsu.find(u) == dsu.find(v))
            
        return ans