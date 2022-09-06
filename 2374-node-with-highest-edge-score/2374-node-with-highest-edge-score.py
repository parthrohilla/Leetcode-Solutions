class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        adj = defaultdict(int)
        for i,node in enumerate(edges):
            adj[node] += i

        score, ans = 0, math.inf
        print(adj)
        for key,value in adj.items():
            if value > score:
                score = value
                ans = key
            if score == value:
                ans = min(ans, key)
        return ans
                
            