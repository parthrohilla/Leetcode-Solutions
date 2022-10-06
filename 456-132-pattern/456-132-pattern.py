class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = -math.inf
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < second: return True
            while stack and stack[-1] < nums[i]:
                second = max(second, stack.pop())
            stack.append(nums[i])
        return False