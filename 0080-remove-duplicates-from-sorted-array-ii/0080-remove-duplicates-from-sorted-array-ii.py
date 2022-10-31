class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front = 2
        for i in range(2, len(nums)):
            if not nums[i] == nums[front-1] == nums[front-2]:
                nums[front] = nums[i]
                front += 1
        return front
                
            