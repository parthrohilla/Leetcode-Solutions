class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [0]*(n+1)
        q = deque()
        for i in range(n+1):
            if not visited[i]:
                q.append((i,1))
                visited[i] = 1
                while q:
                    node, color = q.popleft()
                    for nei in adj[node]:
                        if visited[nei] == 0:
                            visited[nei] = -1 * color
                            q.append((nei,-1*color))
                        elif visited[nei] == color:
                            return False
        return True
        
                