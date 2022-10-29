class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        degrees = defaultdict(int)
        
        for u, v in pairs:
            adj[u].append(v)
            degrees[u] += 1
            degrees[v] -= 1
        
        start = pairs[0][0]
        for node in degrees.keys():
            if degrees[node] == 1:
                start = node
                break
        
        ans = []
        def euler(x):
            while adj[x]:
                euler(adj[x].pop())
            ans.append(x)
        
        euler(start)
        ans = ans[::-1]
        return [ [ans[i], ans[i+1]] for i in range(len(ans)-1) ]