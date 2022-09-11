class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        components = []
        def dfs(i):
            visited.add(i)
            nodes = 1
            for nei in adj[i]:
                if nei not in visited:
                    nodes += dfs(nei)
            return nodes
        
        visited = set()
        ans = (n*(n-1))//2
        for i in range(n):
            if i not in visited:
                temp = dfs(i)
                ans -= (temp*(temp-1))//2
        
        # res = 0
        # print(components)
        # for i in range(len(components)):
        #     for j in range(i+1,len(components)):
        #         res += (components[i]*components[j])
        return ans
        
        