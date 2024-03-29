class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj, q, visited = defaultdict(list), deque(), set()
        # Make adj List
        for u,v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        # Graph coloring for all connected components
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
                            color[nei] = (color[node] + 1) % 4 if (color[node] + 1) > 4 else (color[node] + 1)
                            q.append(nei)
        return color
            