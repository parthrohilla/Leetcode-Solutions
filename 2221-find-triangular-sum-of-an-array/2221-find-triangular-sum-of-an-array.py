class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            temp = []
            for i in range(len(nums)-1):
                a,b = nums[i], nums[i+1]
                temp.append((a+b)%10)
            nums = temp
        return nums[0]
            