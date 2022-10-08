class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj, self.ans, seen, start = defaultdict(list), [], set(), 0
        # DFS Helper for graph traversal
        def dfs(i):
            self.ans.append(i)
            seen.add(i)
            for nei in adj[i]:
                if nei not in seen: 
                    dfs(nei)
            return
        # Create Adjacency List
        for a,b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)
        # Find the degree 1 node - starting point for DFS
        for x in adj:
            if len(adj[x]) == 1:
                start = x        
        # Call DFS to populate path/ans
        dfs(start)
        return self.ans