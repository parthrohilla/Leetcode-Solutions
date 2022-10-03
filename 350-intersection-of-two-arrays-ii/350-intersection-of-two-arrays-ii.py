class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter, ans = Counter(nums2), []
        for n in nums1:
            if counter[n] > 0:
                ans.append(n)
                counter[n] -= 1      
        return ans