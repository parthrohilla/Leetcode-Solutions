class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(i):
            self.ans.append(i)
            seen.add(i)
            for nei in adj[i]:
                if nei not in seen:
                    dfs(nei)
            return
        
        adj = defaultdict(list)
        for a,b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)
        
        self.ans = []
        seen = set()
        start = 0
        for x in adj:
            if len(adj[x]) == 1:
                start = x
        
        dfs(start)
        return self.ans