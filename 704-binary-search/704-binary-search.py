class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(left, right):
            mid = int( (left+right)/2 )
            if left>right:
                return -1
            elif nums[mid] == target:
                return mid
            elif nums[mid]>target:
                return bs(left, mid-1)
            else:
                return bs(mid+1, right)
        
        return bs(0, len(nums)-1)