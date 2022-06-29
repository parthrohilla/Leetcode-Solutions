class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n * (n+1))//2
        for x in nums:
            sum -= x
        return sum