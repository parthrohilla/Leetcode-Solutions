class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n = len(board), len(board[0])
        dir = [ (1,0), (-1,0), (0,-1), (0,1), (-1,1), (1,1), (-1,-1), (1,-1) ]
        
        def helper(x, y):
            count = 0
            for dx, dy in dir:
                i, j = x + dx, y + dy
                if i in range(m) and j in range(n):
                    if board[i][j] == 1 or board[i][j] == 3:
                        count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                alive = helper(i, j)
                if board[i][j]:
                    if alive < 2 or alive > 3:
                        board[i][j] = 1
                    elif alive == 2 or alive == 3:
                        board[i][j] = 3
                elif alive == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] == 2 or board[i][j] == 3:
                    board[i][j] = 1
                    
        
                    
                    
                        
        