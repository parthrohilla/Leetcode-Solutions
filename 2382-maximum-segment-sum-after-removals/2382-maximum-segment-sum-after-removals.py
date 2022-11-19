class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        self.maxSegment = 0
        parent = {}
        total = {}
        
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(u,v):
            U,V = find(u), find(v)
            if U == V: return
            parent[V] = parent[U]
            total[V] += total[U]
            total[U] = total[V]
            self.maxSegment = max(self.maxSegment, total[U])
            
        def mergeSegments(u):
            parent[u] = u
            total[u] = nums[u]
            self.maxSegment = max(self.maxSegment, total[u])
            if u-1 in parent:
                union(u,u-1)
            if u+1 in parent:
                union(u,u+1)
            
        ans = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            ans[i] = self.maxSegment
            removed_index = removeQueries[i]
            mergeSegments(removed_index)
        return ans
            