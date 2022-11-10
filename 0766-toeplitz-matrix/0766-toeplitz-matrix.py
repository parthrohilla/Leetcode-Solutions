class Solution:
    def isToeplitzMatrix(self, M: List[List[int]]) -> bool:
        m, n = len(M), len(M[0]) 
        for i in range(m-1):
            for j in range(n-1):
                if M[i][j] != M[i+1][j+1]: return False
        return True