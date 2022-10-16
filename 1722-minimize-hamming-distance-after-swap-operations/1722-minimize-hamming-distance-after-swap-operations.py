class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = [x for x in range(n)]
        
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            x, y = find(a), find(b)
            if x == y: return
            else: parent[y] = x
        
        for a,b in allowedSwaps:
            union(a,b)
        
        ans = 0
        m = defaultdict(set)
        for i in range(n):
            m[find(i)].add(i)
        
        for indices in m.values():
            sourcecnt = Counter([source[i] for i in indices])
            targetcnt = Counter([target[i] for i in indices])
            diff = sourcecnt - targetcnt
            ans += sum(diff.values())
            
        return ans