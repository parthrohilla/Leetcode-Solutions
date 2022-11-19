class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for k in count:
            if k-1 in count:
                ans = max(ans, count[k] + count[k-1])
        return ans
                
                