class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp = [0] * (n+1)
        temp[0] = -1
        
        for a,b in trust:
            temp[a] -= 1
            temp[b] += 1
        
        for i,num in enumerate(temp):
            if num == n-1:
                return i
            
        return -1