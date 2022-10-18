class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        index = 0
        n = len(nums)
        temp = nums + nums
        for i, num in enumerate(temp):
            while stack and temp[stack[-1]] < num:
                pop = stack.pop()
                ans[pop] = num
            stack.append(i%n)
        return ans