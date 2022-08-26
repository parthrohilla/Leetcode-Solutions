class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        deg = [0] * (n+1)
        for a, b in trust:
            deg[b] += 1
            deg[a] -= 1
        
        for v in range(1, n+1):
            if deg[v] == n-1:
                return v
            
        return -1
        