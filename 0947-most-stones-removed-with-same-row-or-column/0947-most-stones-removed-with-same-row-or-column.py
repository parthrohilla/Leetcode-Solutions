class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {(x,y):(x,y) for (x,y) in stones}
        self.combine = 0
        
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            x, y = find(a), find(b)
            if x == y: return
            self.combine += 1
            parent[y] = x
        
        rows, cols = defaultdict(list), defaultdict(list)
        for i,j in stones:
            if rows[i]: union((i,j), rows[i][0])
            if cols[j]: union((i,j), cols[j][0])
            rows[i].append((i,j))
            cols[j].append((i,j))

        return self.combine
        
            
        