class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i >= rows or i < 0 or j >= cols or j < 0 or visited[i][j] or board[i][j] != word[index]:
                return False

            visited[i][j] = True
            res = (dfs(i+1, j, index+1) or
                   dfs(i-1, j, index+1) or
                   dfs(i, j+1, index+1) or
                   dfs(i, j-1, index+1))

            visited[i][j] = False
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False