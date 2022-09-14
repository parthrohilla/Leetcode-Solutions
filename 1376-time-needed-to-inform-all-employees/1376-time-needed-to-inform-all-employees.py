class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i,m in enumerate(manager):
            if m != -1: adj[m].append(i)
        
        def dfs(i):
            time = 0
            for sub in adj[i]:
                time = max(time,dfs(sub))
            return time + informTime[i]
        
        return dfs(headID)