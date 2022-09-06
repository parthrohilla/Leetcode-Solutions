class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row, col = defaultdict(list), defaultdict(list)
        for i,j in stones:
            row[i].append(j)
            col[j].append(i)
        
        def dfs(i,j):
            points.remove((i,j))
            for x in col[j]:
                if (x,j) in points:
                    dfs(x,j)
            
            for y in row[i]:
                if (i,y) in points:
                    dfs(i,y)
        
        n = len(stones)
        islands = 0
        points = {(i, j) for i, j in stones}
        for i,j in stones:
            if (i,j) in points:
                dfs(i,j)
                islands += 1
        return n - islands
        