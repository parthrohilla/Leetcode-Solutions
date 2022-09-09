class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in redEdges:
            adj[a].append((b,"red"))
        
        for a,b in blueEdges:
            adj[a].append((b,"blue"))
        
        ans, distance = [-1]*n, 0
        ans[0] = 0
        visited = set()
        q = deque()
        q.append((0,"g", 0))
        while q:
            node, color, distance = q.popleft()
            for nei,c in adj[node]:
                if c != color:
                    if ans[nei] == -1: 
                        ans[nei] = distance+1
                    if (nei,c) not in visited:
                        q.append((nei,c, distance+1))
                    visited.add((nei,c))
            # print(q)
        return ans