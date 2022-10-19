class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        n, left = len(nums), [0]*(n)
        total = sum(nums)
        splits = 0
        for i in range(0, n-1):
            left[i] = nums[i] + left[i-1] if i > 0 else nums[i]
            if left[i] >= (total - left[i]):
                print(left[i], total - left[i])
                splits += 1
        return splits