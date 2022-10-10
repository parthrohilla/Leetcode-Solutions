class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        path1, path2 = [-1]*n, [-1]*n
        
        def dfs(i, distance, path):
            path[i] = distance
            nei = edges[i]
            if nei != -1 and path[nei] == -1:
                dfs(nei,distance+1, path)
            
        dfs(node1, 0, path1)
        dfs(node2, 0, path2)
        
        d = math.inf
        ans = -1
        for node in range(n):
            if path1[node] != -1 and path2[node] != -1 and max(path1[node], path2[node]) < d:
                d = max(path1[node], path2[node])
                ans = node
        print(path1, path2)
        return ans
            