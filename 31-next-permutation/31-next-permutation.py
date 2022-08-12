class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i= n-1
        
        while i>0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        
        pivot = i-1
        j = n-1
        while nums[j] <= nums[pivot]:
            j -= 1
        
        nums[j], nums[pivot] = nums[pivot], nums[j]
        l, r = pivot+1, n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        