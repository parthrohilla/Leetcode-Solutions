class Solution:
    def dfs(self,board,index,recursionStack,word,i,j):
        #we will do dfs from the index i,j in order to complete the word on the board
        if index == len(word)-1:
            return True
        recursionStack.add((i,j))
        result = False
        if i > 0:
            if (i-1,j) not in recursionStack and board[i-1][j] == word[index+1]:
                result = result or self.dfs(board,index+1,recursionStack,word,i-1,j)
        if i < len(board)-1:
            if (i+1,j) not in recursionStack and board[i+1][j] == word[index+1]:
                result = result or self.dfs(board,index+1,recursionStack,word,i+1,j)
        if j > 0:
            if (i,j-1) not in recursionStack and board[i][j-1] == word[index+1]:
                result = result or self.dfs(board,index+1,recursionStack,word,i,j-1)
        if j < len(board[0])-1:
            if (i,j+1) not in recursionStack and board[i][j+1] == word[index+1]:
                result = result or self.dfs(board,index+1,recursionStack,word,i,j+1)
        recursionStack.remove((i,j))
        return result
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board,0,set({}),word,i,j):
                        return True
        return False