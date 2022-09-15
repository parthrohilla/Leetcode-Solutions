class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0,0
        for c1,c2 in zip(s1,s2):
            if c1 == "x" and c2 == "y": x_y += 1
            if c1 == "y" and c2 == "x": y_x += 1
            
        swaps = 0
        swaps = x_y//2 + y_x//2
        
        x_y = x_y % 2
        y_x = y_x % 2
        
        if (y_x+x_y) % 2 == 1:
            return -1
        
        swaps += (y_x+x_y)
        return swaps