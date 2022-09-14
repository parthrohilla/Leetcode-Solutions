class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n,visit=len(edges),set()
        ranks=[float('inf')]*n

        def t(i,rank):
            if i in visit or edges[i]==-1: 
                return -1

            if ranks[i]<rank: 
                return rank-ranks[i]

            ranks[i]=rank
            val=t(edges[i],rank+1)
            visit.add(i)
            return val

        return max(t(i,0) for i in range(n))