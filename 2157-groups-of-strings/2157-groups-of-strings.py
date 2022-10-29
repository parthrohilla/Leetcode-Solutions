class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.sizes = [1]*n
        self.combined = 0
    
    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y: return
        self.parent[y] = x
        self.sizes[x] += self.sizes[y]
        self.sizes[y] = 0
        self.combined += 1
        
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        seen = {}
        dsu = DSU(len(words))
        
        for i, word in enumerate(words):
            bitset = sum(1 << (ord(char)-ord("a")) for char in word)
            if bitset in seen:
                dsu.union(i, seen[bitset])
            
            for j in range(26):
                if bitset & (1 << j):
                    after_removing_set = bitset ^ (1 << j)
                    if after_removing_set in seen:
                        dsu.union(i, seen[after_removing_set])
                    seen[after_removing_set] = i
            seen[bitset] = i
        
        return [len(words) - dsu.combined, max(dsu.sizes)]