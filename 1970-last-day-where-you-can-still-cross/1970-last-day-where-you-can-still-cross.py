class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # DSU Functions 
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return
            parent[y] = x
            
        parent = {}
        for i in range(row):
            for j in range(col):
                parent[(i,j)] = (i,j)
        
        left, right = -1, -2
        parent[left] = left
        parent[right] = right
        directions = [[-1,0], [1,0], [0,-1], [0,1], [-1,1], [1,1], [-1,-1], [1,-1]]
        seen = set()
        
        for t, (x,y) in enumerate(cells):
            y -= 1
            x -= 1
            
            for dx, dy in directions:
                i, j = x + dx, y + dy
                
                if 0 <= i < row:
                    if 0 <= j < col:
                        if (i,j) in seen:
                            union((i,j), (x,y))
                    else:
                        if j == -1:
                            union((x,y), left)
                        if j == col:
                            union((x,y), right)
                            
                if find(left) == find(right):
                    return t
                
            seen.add((x,y))
                
        return t
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            