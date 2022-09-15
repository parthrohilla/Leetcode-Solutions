class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        countx, counto, i = set(), set(), 0
        
        def iswinner(char, seen):
            for i in range(3):
                if (i,0) in seen and (i,1) in seen and (i,2) in seen: return True
                elif (0,i) in seen and (1,i) in seen and (2,i) in seen: return True
            if (0,0) in seen and (1,1) in seen and (2,2) in seen: return True
            if (2,0) in seen and (1,1) in seen and (0,2) in seen: return True
            return False
        
        for r,c in (moves):
            if i % 2 == 1: counto.add((r,c))
            else: countx.add((r,c))
                
            if len(countx) >= 3:
                if iswinner("x", countx):
                    return "A"
            if len(counto) >= 3:
                if iswinner("o", counto):
                    return "B"
            i += 1
        
        if len(countx) + len(counto) == 9: return "Draw"
        else: return "Pending"