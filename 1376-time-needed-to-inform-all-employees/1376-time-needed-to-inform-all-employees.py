class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i,m in enumerate(manager):
            if m == -1: continue
            adj[m].append(i)
        
        def dfs(i):
            x = 0
            for sub in adj[i]:
                x = max(x,dfs(sub))
            return x + informTime[i]
        
        return dfs(headID)