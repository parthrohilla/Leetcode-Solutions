class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj, deg = defaultdict(list), [0]*n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            deg[a] += 1
            deg[b] += 1
        
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
        ans = []        
        while q:
            ans = []
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)
                ans.append(node)
        return ans
            