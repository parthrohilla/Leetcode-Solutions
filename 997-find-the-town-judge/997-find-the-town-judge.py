class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp = [0] * (n+1)
        for a,b in trust:
            temp[a] -= 1
            temp[b] += 1
        
        for i in range(1,n+1):
            if temp[i] == n-1:
                return i
            
        return -1