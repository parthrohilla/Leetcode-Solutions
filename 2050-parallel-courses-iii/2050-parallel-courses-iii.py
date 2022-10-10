class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0]*n
        adj = defaultdict(list)
        for u,v in relations:
            adj[u-1].append(v-1)
            indegree[v-1] += 1
        
        h = []
        heapq.heapify(h)
        for node in range(n):
            if indegree[node] == 0:
                heapq.heappush(h, (time[node], node))
        
        
        completed = 0
        while len(h) > 0:
            t, i = heapq.heappop(h)
            completed += 1
            
            if completed == n: 
                return t
            
            for v in adj[i]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    heapq.heappush(h, (t + time[v], v))
        
        return 0
            
            
        
        
        