class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def find_unassigned():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return (i,j)
            return (-1,-1)
        
        def helper():
            i,j = find_unassigned()
            if (i,j) == (-1,-1):
                return True
            
            for k in range(1,10):
                val = str(k)
                if self.isvalid(i,j,board,val):
                    board[i][j] = str(val)
                    if helper():
                        return True
                    board[i][j] = "."
            return False
            
        
        helper()
        #End of function 
        
    def isvalid(self,x,y,board,val):
        seen = set()
        seen.add(val)
        for i in range(9):
            if board[i][y] in seen:
                return False
            if board[i][y] != ".":
                seen.add(board[i][y])
        
        seen.clear()
        seen.add(val)
        for j in range(9):
            if board[x][j] in seen:
                return False
            if board[x][j] != ".":
                seen.add(board[x][j])
        
        seen.clear()
        seen.add(val)
        row_start = x - x%3
        col_start = y - y%3
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if board[i][j] in seen:
                    return False
                if board[i][j] != ".":
                    seen.add(board[i][j])
        
        return True
        
        