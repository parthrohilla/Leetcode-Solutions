class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[math.inf]*n for _ in range(n)]
        # Populating matrix with trivial values
        for i in range(n):
            matrix[i][i] = 0
        for a,b,weight in edges:
            matrix[a][b] = weight
            matrix[b][a] = weight
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        
        ans, node = math.inf, 0
        for i in range(n):
            nei = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold and i != j:
                    nei += 1
            print(i, nei)
            if nei <= ans:
                ans = nei
                node = i
        return node
        
        