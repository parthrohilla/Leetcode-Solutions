class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        e = defaultdict(list)
        er = defaultdict(list)
        for a,b,w in edges:
            e[a].append([b,w])
            er[b].append([a,w])
        
        
        def shortest(adj,src):
            distance = [math.inf]*n
            distance[src] = 0
            heap = [[0,src]]
            while heap:
                d,node = heapq.heappop(heap)
                if d > distance[node]: continue
                for nei,w in adj[node]:
                    if distance[nei] > d + w:
                        distance[nei] = d + w
                        heapq.heappush(heap,[distance[nei],nei])
            return distance
        
        d1 = shortest(e,src1)
        d2 = shortest(e,src2)
        dd = shortest(er,dest)
        
        d = math.inf
        for i in range(n):
            d = min(d,d1[i] + d2[i] + dd[i])
        return -1 if d >= math.inf else d
        