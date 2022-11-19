class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count, ans = Counter(nums), 0
        for key in count:
            if key-1 in count:
                ans = max(ans, count[key] + count[key-1])
        return ans
                
                