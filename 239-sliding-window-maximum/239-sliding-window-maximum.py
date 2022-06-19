class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l, r = 0, 0
        
        output = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            # Removing left most if out of window bounds
            if l > q[0]:
                q.popleft()
            # Adding to output
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
            
        return output