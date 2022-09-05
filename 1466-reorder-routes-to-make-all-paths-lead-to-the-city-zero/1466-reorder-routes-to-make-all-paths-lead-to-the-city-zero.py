class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in connections:
            adj[a].append([b, (a,b)])
            adj[b].append([a, (a,b)])
        
        visited = set()
        q, changed = deque(), 0
        q.append(0)
        
        while q:
            node = q.popleft()
            visited.add(node)
            
            for nei, direction in adj[node]:
                if nei not in visited:
                    if (node,nei) == direction:
                        changed += 1
                    q.append(nei)
        return changed