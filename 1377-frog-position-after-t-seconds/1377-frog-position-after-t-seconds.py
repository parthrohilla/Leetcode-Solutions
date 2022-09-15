class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if target == 1 and len(edges) == 0: return 1
        if target == 1 and t>0: return 0
        
        adj, seen, level = defaultdict(list), {1}, 0
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        q = deque()
        q.append((1,1))
        while q:
            level += 1
            for _ in range(len(q)):
                n,p = q.popleft()
                children = sum([1 if x not in seen else 0 for x in adj[n]])
                
                for nei in adj[n]:
                    if nei == target:
                        if t < level: return 0
                        elif t == level: return p*(1/children)
                        else:
                            k = sum([1 if x not in seen else 0 for x in adj[nei]])
                            if k == 0: return p*(1/children)
                            else: return 0
                    elif nei not in seen:
                        seen.add(nei)
                        q.append((nei,p*(1/children)))
        return 0
                        
                        