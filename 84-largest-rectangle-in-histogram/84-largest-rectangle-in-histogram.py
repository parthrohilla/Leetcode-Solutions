class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        
        # populate left and right
        stack = []
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                pop = stack.pop()
                right[pop] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]:
                pop = stack.pop()
                left[pop] = i
            stack.append(i)
            
        # calculate ans
        area = 0
        for i,h in enumerate(heights):
            width = right[i] - left[i] - 1
            area = max(area, width * h)
        return area