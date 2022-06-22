class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums)-1
        
        while l<=r:
            mid = (l+r) // 2
            if mid>=1 and mid<len(nums)-1 and nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return nums[mid]
            elif nums[l]<=nums[mid]:
                if nums[mid]<=nums[r]:
                    return nums[l]
                else:
                    l = mid+1
            else:
                r = mid-1
        return nums[l]