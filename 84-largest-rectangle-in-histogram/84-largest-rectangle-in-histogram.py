class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]: right[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]: left[stack.pop()] = i
            stack.append(i)
        
        area = 0
        print(left, right)
        for i,h in enumerate(heights):
            base = right[i]-left[i]-1
            area = max(area, h*base)
        return area
        
        