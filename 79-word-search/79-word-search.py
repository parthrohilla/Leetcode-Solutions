class Solution:
    def dfs(self, board: List[List[str]], word: str, i: int, j: int, visited: List[List[bool]], k: int) -> bool:
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k] or visited[i][j]: 
            return False
        visited[i][j] = True
        res1 = self.dfs(board, word, i + 1, j, visited, k + 1)
        res2 = self.dfs(board, word, i - 1, j, visited, k + 1)
        res3 = self.dfs(board, word, i, j + 1, visited, k + 1)
        res4 = self.dfs(board, word, i, j - 1, visited, k + 1)
        visited[i][j] = False
        return (res1 or res2 or res3 or res4)
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                k = 0
                if self.dfs(board, word, i, j, visited, k):
                    return True
        return False