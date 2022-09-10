class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n, start = len(graph), 0
        q = deque()
        visited = set()
        final = ((1<<n) - 1)
        k = min([len(x) for x in graph])
        for i in range(n):
            if len(graph[i]) == k:
                visited.add((i,1<<i))
                q.append((i,1<<i))
        
        distance = 0
        while q:
            distance += 1
            for _ in range(len(q)):
                node,state = q.popleft()
                for nei in graph[node]:
                    new_state = state | (1<<nei)
                    if new_state == final:
                        return distance
                    if (nei, new_state) in visited:
                        continue
                    q.append((nei, new_state))
                    visited.add((nei, new_state))
        return 0
    