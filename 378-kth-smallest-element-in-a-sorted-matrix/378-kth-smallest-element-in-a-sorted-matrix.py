class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def count(m):
            count = 0
            for row in matrix:
                count += bisect_right(row, m)
            return count
        
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]
        while l<r:
            mid = (l+r) // 2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid
        return l