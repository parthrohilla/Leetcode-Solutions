class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_set, col_set = [False]*rows, [False]*cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set[i], col_set[j] = True, True
        
        for i in range(rows):
            for j in range(cols):
                if row_set[i] or col_set[j]:
                    matrix[i][j] = 0
        