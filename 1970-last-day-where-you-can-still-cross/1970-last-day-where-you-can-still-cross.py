class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # DSU Implementation 
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return
            parent[y] = x
        
        # Setting each cell as it's own parent before we start to Union anuy Cells
        parent, seen = {}, set()
        for i in range(row):
            for j in range(col):
                parent[(i,j)] = (i,j)
        
        # Declaring important Variables
        left, right = -1, -2
        parent[left], parent[right] = left, right
        directions = [[-1,0], [1,0], [0,-1], [0,1], [-1,1], [1,1], [-1,-1], [1,-1]]
        
        # We Try to union any 2 connected water(flooded) cells as we traverse 
        for t, (x,y) in enumerate(cells):
            x -= 1
            y -= 1
            for dx, dy in directions:
                i, j = x + dx, y + dy
                if i in range(row):
                    if j in range(col):
                        if (i,j) in seen: union((i,j), (x,y))
                    else:
                        if j == -1: union((x,y), left)
                        if j == col: union((x,y), right)
                # If left and right Parts are connected then we can't move from top to bottom            
                if find(left) == find(right):
                    return t
            # Adding the flooded cells     
            seen.add((x,y))
                
        return t
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            