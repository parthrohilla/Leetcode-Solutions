class Solution:
    def minCost(self, graph: List[List[int]]) -> int:
        m, n = len(graph), len(graph[0])
        dp = [[math.inf]*n for _ in range(m)]
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        q = deque()
        q.append((0,0))
        dp[0][0] = 0
        while q:
            x,y = q.popleft()
            arrow = graph[x][y]
            for i in range(4):
                dx, dy = directions[i][0], directions[i][1]
                if 0<=x + dx<m and 0<=y + dy<n:
                    if i + 1 == arrow and dp[x+dx][y+dy] > dp[x][y]:
                        dp[x+dx][y+dy] = dp[x][y]
                        q.append((x+dx, y+dy))
                    elif dp[x][y] + 1 < dp[x+dx][y+dy]:
                        dp[x+dx][y+dy] = 1 + dp[x][y]
                        q.append((x+dx, y+dy))
        return dp[m-1][n-1]
            