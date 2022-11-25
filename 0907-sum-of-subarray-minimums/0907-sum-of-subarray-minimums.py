class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1000000007

        # Right boundary of i, where arr[i] is the minima.
        leftToRight = [len(arr)] * len(arr)
        
        # Going from left to right to find the right boundary.
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                leftToRight[stack.pop()] = i
            stack.append(i)
        
        # Left boundary of i, where arr[i] is the minima.
        rightToLeft = [-1] * len(arr)
        # Going from right to left to find the left boundary.
        stack = []
        for i in reversed(range(len(arr))):
            while stack and arr[i] < arr[stack[-1]]:
                rightToLeft[stack.pop()] = i
            stack.append(i)

        res = 0
        # Compute the result.
        for idx in range(len(arr)):
            l, r = rightToLeft[idx], leftToRight[idx]
            res += (r-idx) * (idx-l) * arr[idx]
            res %= mod
            
        return res
                
        