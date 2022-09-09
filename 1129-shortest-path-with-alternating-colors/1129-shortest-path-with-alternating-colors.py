class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj, ans = defaultdict(list), [-1]*n
        # Create an adjacency list with (TARGET, COLOUR_OF EDGE)
        for a,b in redEdges: adj[a].append((b,"red"))
        for a,b in blueEdges: adj[a].append((b,"blue"))
            
        ans[0], distance, visited, q = 0, 0, set(), deque()
        q.append((0,"any_color", 0))
        while q:
            node, color, distance = q.popleft()
            for nei,c in adj[node]:
                if c != color:
                    if ans[nei] == -1: 
                        ans[nei] = distance+1
                    if (nei,c) not in visited:
                        q.append((nei,c, distance+1))
                        visited.add((nei,c))
        return ans