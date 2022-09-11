class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i,parent = -1):
            nonlocal timer
            discovery[i], low[i] = timer, timer
            timer += 1
            for nei in adj[i]:
                if nei == parent:
                    continue
                # Tree - Edge
                elif discovery[nei] == -1:
                    dfs(nei,i)
                    low[i] = min(low[i], low[nei])
                    if low[nei] > discovery[i]:
                        ans.append([i,nei])
                # Back - Edge
                else:
                    low[i] = min(low[i], low[nei])
            
        
        ans, discovery, low = [], [-1]*n, [-1]*n
        timer = 0
        for i in range(n):
            if discovery[i] == -1:
                dfs(i)
        return ans