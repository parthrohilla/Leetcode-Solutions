class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]}
        config = "".join(map(str,board[0])) + "".join(map(str,board[1]))
        
        Q = deque()
        Q.append([config, 0])
        seen = set([config])
        
        while Q:
            current_config, d = Q.popleft()
            
            if current_config == "123450":
                return d
            
            for i, char in enumerate(current_config):
                if char == "0":
                    for j in moves[i]:
                        T = list(current_config)
                        T[i], T[j] = T[j], T[i]
                        new_config = "".join(T)
                        if new_config not in seen:
                            Q.append([new_config, d+1])
                            seen.add(new_config)
                    
        return -1
            