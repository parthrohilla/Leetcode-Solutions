class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t,index = stack.pop()
                output[index] = i - index
            stack.append([temp,i])
        
        return output