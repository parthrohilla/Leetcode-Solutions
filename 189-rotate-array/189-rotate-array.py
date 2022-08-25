class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        ans = [0] * n
        for i,num in enumerate(nums):
            ans[(i+k) % n] = nums[i]
        for i in range(n):
            nums[i] = ans[i]
        
        