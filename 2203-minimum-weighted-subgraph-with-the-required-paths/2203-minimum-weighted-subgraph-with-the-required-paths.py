class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        e, er = defaultdict(list), defaultdict(list)
        for a,b,w in edges:
            e[a].append([b,w])
            er[b].append([a,w])
        
        
        def djiktras(adj,src):
            distance, heap, visited = [math.inf]*n, [[0,src]], set()
            distance[src] = 0
            
            while heap:
                d,node = heapq.heappop(heap)   
                if node in visited: continue
                visited.add(node)
                for nei,w in adj[node]:
                    if nei not in visited:
                        if distance[nei] > d + w:
                            distance[nei] = d + w
                            heapq.heappush(heap,[distance[nei],nei])
            return distance
        
        
        d1 = djiktras(e,src1)
        d2 = djiktras(e,src2)
        dd = djiktras(er,dest)
        
        ans = math.inf
        for i in range(n):
            ans = min(ans,d1[i] + d2[i] + dd[i])
        return -1 if ans >= math.inf else ans
        