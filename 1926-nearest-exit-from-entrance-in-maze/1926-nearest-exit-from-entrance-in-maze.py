class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n,q = len(maze), len(maze[0]), deque()
        q.append((entrance[0], entrance[1]))
        visited = {(entrance[0], entrance[1])}
        
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    x,y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and (x,y) not in visited and maze[x][y] == ".":
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            return steps
                        else:
                            q.append((x,y))
                            visited.add((x,y))
        return -1