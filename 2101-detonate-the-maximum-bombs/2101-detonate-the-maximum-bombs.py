class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, adj, visited, ans = len(bombs), defaultdict(list), set(), 0
        # DFS Method
        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)
        # Building adjacency list
        for i in range(n):
            for j in range(n):
                if i != j:
                    ax,ay,ar = bombs[i]
                    bx,by,br = bombs[j]
                    if (ax-bx)**2 + (ay-by)**2 <= ar**2: 
                        adj[i].append(j)
        # checking detonations from each bomb
        for bomb in range(n):
            visited = set()
            dfs(bomb)
            ans = max(ans, len(visited))
        return ans