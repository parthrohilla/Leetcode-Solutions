class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        D = [set() for _ in range(n+1)]
        D[1].add(0)
        adj = defaultdict(list)
        heap = [(0, 1)]
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        while heap:
            curr_time, i = heapq.heappop(heap)
            if i == n and len(D[n]) == 2: return max(list(D[n]))
            
            signal = curr_time // change
            for nei in adj[i]:
                if signal % 2 == 1:
                    curr_time += (change*(signal+1) - curr_time)
                
                if not D[nei] or len(D[nei]) < 2:
                    D[nei].add(curr_time + time)
                    heapq.heappush(heap, (curr_time + time, nei))
            
        return -1