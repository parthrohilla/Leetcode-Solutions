class Solution:
    def minCost(self, graph: List[List[int]]) -> int:
        m, n, q = len(graph), len(graph[0]), deque()
        dp, directions = [[math.inf]*n for _ in range(m)], [[0,1], [0,-1], [1,0], [-1,0]]
        
        q.append((0,0))
        dp[0][0] = 0
        while q:
            x,y = q.popleft()
            arrow = graph[x][y]
            for i in range(4):
                new_x, new_y = x+directions[i][0], y+directions[i][1]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if i + 1 == arrow and dp[new_x][new_y] > dp[x][y]:
                        dp[new_x][new_y] = dp[x][y]
                        q.append((new_x, new_y))
                    elif dp[x][y] + 1 < dp[new_x][new_y]:
                        dp[new_x][new_y] = 1 + dp[x][y]
                        q.append((new_x, new_y))
        return dp[m-1][n-1]
            