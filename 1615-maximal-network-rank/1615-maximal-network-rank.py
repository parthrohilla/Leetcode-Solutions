class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if i in adj[j]:
                    ans = max(ans, len(adj[i]) + len(adj[j]) -1)
                else:
                    ans = max(ans, len(adj[i]) + len(adj[j]))          
        return ans