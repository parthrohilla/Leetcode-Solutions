class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source, target = 0, n-1
        
        def dfs(i, path):
            path = path + [i]
            if i == target:
                ans.append(path)
                return
            
            for u in graph[i]:
                    dfs(u, path)
        
        ans = []
        dfs(source, [])
        return ans