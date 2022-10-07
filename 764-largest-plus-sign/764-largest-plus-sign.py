class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1]*n for _ in range(n)]
        for i,j in mines: grid[i][j] = 0
            
        dp1, dp2, dp3, dp4 = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)], [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        
        for i in range(n):
            temp = 0
            for j in range(n):
                if grid[i][j] == 1: temp += 1
                else: temp = 0
                dp1[i][j] = temp
        
        for i in range(n):
            temp = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 1: temp += 1
                else: temp = 0
                dp2[i][j] = temp
        
        for j in range(n):
            temp = 0
            for i in range(n):
                if grid[i][j] == 1: temp += 1
                else: temp = 0
                dp3[i][j] = temp
        
        for j in range(n):
            temp = 0
            for i in range(n-1, -1,-1):
                if grid[i][j] == 1: temp += 1
                else: temp = 0
                dp4[i][j] = temp
        
        ans = 0
        for i in range(n):
            for j in range(n):
                sign = min(dp1[i][j], dp2[i][j], dp3[i][j], dp4[i][j])
                ans = max(ans, sign)
        return ans
        
        