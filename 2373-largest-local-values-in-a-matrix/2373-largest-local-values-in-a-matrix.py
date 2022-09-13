class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[0,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
        
        n = len(grid)
        output = [[0]*(n-2) for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                temp = 0
                for dx,dy in directions:
                    x,y = i+dx,j+dy
                    temp = max(temp,grid[x][y])
                temp = max(temp,grid[i][j])
                output[i-1][j-1] = temp
        return output