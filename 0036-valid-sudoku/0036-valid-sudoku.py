class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = set(), set(), set()
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                
                rowKey = (i, board[i][j])
                colKey = (j, board[i][j])
                sqk = (i//3, j//3, board[i][j])
                
                if rowKey in row or colKey in col or sqk in square:
                    return False
                
                row.add(rowKey)
                col.add(colKey)
                square.add(sqk)
        return True