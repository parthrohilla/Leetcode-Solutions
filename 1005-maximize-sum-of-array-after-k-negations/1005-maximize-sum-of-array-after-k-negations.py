class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            if n == 0 or k == 0:
                return sum(nums)
            elif n < 0:
                nums[i] *= -1
                k -= 1
            else:
                if k % 2 == 0:
                    return sum(nums)
                else:
                    return sum(nums) - 2*min(map(abs,nums))
        
        if k % 2 == 1:
            return sum(nums) - 2*min(nums)
        else:
            return sum(nums)