class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]
        col_set, neg_diagonal, pos_diagonal = set(), set(), set()
        count = 0

        def backTrack(row):
            nonlocal count
            if row == n:
                count += 1
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
        return count

    def isNotSafe(self, col_set, pos_diagonal, neg_diagonal, row, col) -> bool:
        if col in col_set or (row + col) in pos_diagonal or (row - col) in neg_diagonal:
            return True
        else:
            return False