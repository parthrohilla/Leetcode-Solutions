class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = [x for x in range(n+1)]
        
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return
            parent[y] = x
            
        
        for x in range(threshold + 1, n+1):
            k = x
            while k <= n:
                union(x, k)
                k += x
        
        return [find(x) == find(y) for x, y in queries]
                