class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(edges)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            if len(adj[a]) == n:
                return a
            if len(adj[b]) == n:
                return b
        