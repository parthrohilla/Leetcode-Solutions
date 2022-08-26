class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for a, b in trust:
            adj[a].append(b)
        
        temp = -1
        for i in range(1, n+1):
            if len(adj[i]) == 0:
                temp = i
                break
                
        for i in range(1, n+1):
            if i != temp and temp not in adj[i]:
                return -1
            else:
                continue
        
        return temp