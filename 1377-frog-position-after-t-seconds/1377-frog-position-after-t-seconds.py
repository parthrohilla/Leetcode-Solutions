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
                children = len([x for x in adj[n] if x not in seen])
                
                for nei in adj[n]:
                    if nei == target:
                        if t < level: return 0
                        elif t == level: return p*(1/children)
                        else:
                            k = len([x for x in adj[nei] if x not in seen])
                            if k == 0: return p*(1/children)
                            else: return 0
                    elif nei not in seen:
                        seen.add(nei)
                        q.append((nei,p*(1/children)))
        return 0
                        
                        