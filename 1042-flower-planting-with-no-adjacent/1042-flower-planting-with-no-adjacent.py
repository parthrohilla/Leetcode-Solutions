class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
            
        q = deque()
        visited = set()
        color = [0]*n
        for u in range(n):
            if u not in visited:
                q.append(u)
                color[u] = 1
                while q:
                    node = q.popleft()
                    visited.add(node)
                    for nei in adj[node]:
                        if color[nei] == 0 or color[nei] == color[node]:
                            color[nei] = color[node] + 1
                            if color[nei] > 4: color[nei] %= 4
                            q.append(nei)
        return color
            