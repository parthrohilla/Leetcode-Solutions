class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.k, self.n, self.adj, indegrees = k, n, defaultdict(list), [0] * n
        for u,v in relations:
            self.adj[u-1].append(v-1)
            indegrees[v-1] += 1
        mask = (1 << self.n) - 1 #1(set-bit) means NOT-Taken, so initially all 0 to (n-1) nodes are 1 
        return self.dfs(mask, tuple(indegrees))
    
    @lru_cache(None)
    def dfs(self, bitmask, indegrees):
        if not bitmask: return 0
        nodes = [x for x in range(self.n) if bitmask & (1 << x) and indegrees[x] == 0]
        ans = math.inf
        for courses_taken in combinations(nodes, min(self.k, len(nodes))):
            new_bitmask, new_indegrees = bitmask, list(indegrees)
            for c in courses_taken:
                new_bitmask ^= (1<<c)
                for nei in self.adj[c]:
                    new_indegrees[nei] -= 1        
            ans = min(ans, 1 + self.dfs(new_bitmask, tuple(new_indegrees)))
        return ans