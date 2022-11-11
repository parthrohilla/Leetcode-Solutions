class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            if n == 0 or k == 0: return sum(nums)
            elif n > 0: break
            else:
                nums[i] *= -1
                k -= 1
        
        return sum(nums) - ( k % 2) * 2 *min(nums)