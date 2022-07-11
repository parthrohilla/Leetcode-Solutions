class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        col_set, neg_diagonal, pos_diagonal = set(), set(), set()
        output = []

        def backTrack(row):
            if row == n:
                temp = ["".join(row) for row in board]
                output.append(temp)
                return

            for col in range(n):
                if self.isNotSafe(col_set, pos_diagonal, neg_diagonal, row, col):
                    continue
                else:
                    col_set.add(col)
                    pos_diagonal.add(row+col)
                    neg_diagonal.add(row-col)
                    board[row][col] = "Q"

                    backTrack(row+1)

                    board[row][col] = "."
                    col_set.remove(col)
                    pos_diagonal.remove(row + col)
                    neg_diagonal.remove(row - col)

        backTrack(0)
        return output

    def isNotSafe(self, col_set, pos_diagonal, neg_diagonal, row, col):
        if col in col_set or (row + col) in pos_diagonal or (row - col) in neg_diagonal:
            return True
        else:
            return False