class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        n = len(patience)
        Q = deque()
        time = [math.inf]*n
        
        time[0] = 0
        Q.append([0,0])
        while Q:
            node, t = Q.popleft()
            for nei in G[node]:
                if time[nei] == math.inf:
                    time[nei] = t + 1
                    Q.append([nei,time[nei]])
        
        res = 0
        for i in range(1,n):
            t = 2 * time[i]
            temp = 0
            if t % patience[i] == 0: temp = (2*t - patience[i])
            else: temp = (2*t - t % patience[i])
            res = max(res, temp)
        return res + 1