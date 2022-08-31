class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land), len(land[0])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        def dfs(i,j):
            nonlocal rb_x, rb_y
            if i<0 or i>=m or j<0 or j>=n or land[i][j] != 1:
                return
            
            land[i][j] = -1
            rb_x, rb_y = max(rb_x, i), max(rb_y, j)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                dfs(x,y)
            return
                
        
        result = []
        rb_x, rb_y = -1, -1
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    rb_x, rb_y = -1, -1
                    dfs(i,j)
                    result.append([i,j,rb_x,rb_y])
        return result