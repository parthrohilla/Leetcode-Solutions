class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        row = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    row[j] += 1
                else:
                    row[j] = 0
            ans = max(ans, self.largestRectangleArea(row))
        return ans
            
    
    def largestRectangleArea(self, heights):
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
        