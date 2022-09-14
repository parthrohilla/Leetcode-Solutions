class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n,visit=len(edges),set()
        ranks=[math.inf]*n

        # i is the node and k is the position in the current cycle, position would be needed to calculate the cycle-length
        def dfs(i,k):
            # if a node is already visited as part of a previous cycle we return -1
            # if edges[i] == -1 means that if it is the last node in a traversal, no need to call dfs() forther since there won't be any cycles found
            if i in visit or edges[i]==-1: 
                return -1
            # Since ranks maintains the first position the node was seen, if we visite it again it means that we have encountered a cycle
            if ranks[i]<k: 
                return k-ranks[i]
            # if cycle not found then update rank and call dfs() from the neighbour and mark the current node as visited
            ranks[i] = k
            val = dfs(edges[i],k+1)
            visit.add(i)
            return val

        # Call dfs() on every node starting from 0
        return max(dfs(i,0) for i in range(n))