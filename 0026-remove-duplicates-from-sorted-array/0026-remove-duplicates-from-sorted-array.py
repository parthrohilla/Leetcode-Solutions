class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[front-1]:
                nums[front] = nums[i]
                front += 1
        return front