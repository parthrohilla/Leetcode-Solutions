class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [x for x in range(n)]
        
        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            x, y = find(a), find(b)
            if x == y: return
            else: parent[y] = x
        
        for a,b in pairs:
            union(a,b)
            
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(s[i])
        
        for key in groups.keys():
            groups[key] = deque(sorted(groups[key]))
        
        ans = ""
        for i in range(n):
            g = find(i)
            char = groups[g].popleft()
            ans += char
        return ans