class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        ans = [[-1]*n for _ in range(m)]
        count_1 = 0
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    count_1 += 1
                else:
                    q.append((i,j))
                    ans[i][j] = 0
        
        d = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q:
            k = len(q)
            d += 1
            for _ in range(k):
                x,y = q.popleft()
                for dx, dy in directions:
                    a, b = x + dx, y + dy
                    if a>=0 and a<m and b>=0 and b<n and ans[a][b] == -1:
                        if matrix[a][b] == 1:
                            ans[a][b] = d
                            count_1 -= 1
                            if count_1 == 0:
                                return ans
                            else:
                                q.append((a,b))
        return ans
                            
                        
                
        