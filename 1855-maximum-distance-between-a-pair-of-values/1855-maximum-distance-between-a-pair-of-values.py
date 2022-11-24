class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        ans = 0
        
        while i < n and j < m:
            if nums1[i] > nums2[j]: 
                i += 1
            else:
                ans = max(ans, j - i)
                j += 1
        return ans