class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        merged = []
        ans = 0
        
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        
        while p1<len(nums1):
            merged.append(nums1[p1])
            p1 +=1
        
        while p2<len(nums2):
            merged.append(nums2[p2])
            p2 +=1
        
        n = len(merged)
        if n % 2 == 1:
            ans = merged[n//2]
        else:
            #[1,2,3,4,5,6]
            ans = (merged[n//2] + merged[n//2-1]) / 2
        
        return ans