class Solution:
    def isToeplitzMatrix(self, M: List[List[int]]) -> bool:
        m, n = len(M), len(M[0])
        
        for i in range(m):
            for j in range(n):
                for k in range(n):
                    if i + k >= m or j + k >= n:
                        break
                    elif M[i][j] != M[i+k][j+k]:
                        return False
        
        return True