class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        G = defaultdict(list)
        for u,v,w in edges:
            G[u].append([v,w])
            G[v].append([u,w])
            
        def dfs(current, path, left):
            # We calculate the total path quality when we reach Node 0
            # So the most trivial case would be when we just call dfs() the first time
            # Later on, if we end up tracking back to Node 0 Again, we have a candidate for a "valid path"
            # So we add up values for all the nodes in the set
            # We continue our dfs() until we have some time left
            if current == 0:
                tmp = 0
                for node in path:
                    tmp += values[node]
                self.best = max(self.best, tmp)
            # Moving to neighbour nodes and calling dfs() until time left
            for nei, wei in G[current]:
                if wei <= left:
                    dfs(nei, {nei} | path, left - wei)
        
        self.best = 0
        # Calling helper dfs() method
        # arguments signify : current node, current path set, time left 
        dfs(0, {0}, maxTime)
        return self.best