class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n-1):
                a,b = nums[i], nums[i+1]
                nums[i] = (a+b) % 10
            n-=1
        return nums[0]
            