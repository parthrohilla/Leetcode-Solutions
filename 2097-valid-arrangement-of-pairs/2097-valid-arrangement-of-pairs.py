class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        out_degrees = defaultdict(int)
        
        for u, v in pairs:
            adj[u].append(v)
            out_degrees[u] += 1
            out_degrees[v] -= 1
        
        start = pairs[0][0]
        for node in out_degrees.keys():
            if out_degrees[node] == 1:
                start = node
                break
        
        ans = []
        def euler_path(x):
            while adj[x]:
                euler_path(adj[x].pop())
            ans.append(x)
        
        euler_path(start)
        ans = ans[::-1]
        return [ [ans[i], ans[i+1]] for i in range(len(ans)-1) ]