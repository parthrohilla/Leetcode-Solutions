class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [1]*n
    
    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y: return
        self.parent[y] = x
        self.size[x] += self.size[y]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def get_factors(n):
            factors = set([n])
            i = 2
            while i*i <= n:
                if n % i == 0:
                    factors.add(i)
                    factors.add(n // i)
                i += 1
            return factors
        
        factor_map = defaultdict(list)
        for i, num in enumerate(nums):
            factors = get_factors(num)
            for f in factors:
                factor_map[f].append(i)
        
        dsu = DSU(len(nums))
        for edges in factor_map.values():
            for i in range(1, len(edges)):
                dsu.union(edges[i-1], edges[i])
        
        return max(dsu.size)