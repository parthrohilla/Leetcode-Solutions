class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n,q = len(isWater), len(isWater[0]), deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1: 
                    isWater[i][j] = 0
                    q.append((i,j))
                else:
                    isWater[i][j] = -1

        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and isWater[x][y]==-1:
                        isWater[x][y] = level
                        q.append((x,y))
        
        return isWater