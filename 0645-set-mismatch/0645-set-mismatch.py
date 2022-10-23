class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = [0, 0]
        
        for n in nums:
            if n in seen: ans[0] = n
            else: seen.add(n)
                
        for i in range(1, len(nums)+1):
            if i not in seen:
                ans[1] = i
                break
        
        return ans