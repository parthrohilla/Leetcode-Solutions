class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, stack = [-1] * n, []
        temp = nums + nums
        for i, num in enumerate(temp):
            while stack and temp[stack[-1]] < num:
                pop = stack.pop()
                ans[pop] = num
            stack.append(i%n)
        return ans