class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0]*(101)
        for n in nums:
            bucket[n] += 1
        ans = []
        for n in nums:
            ans.append(sum(bucket[:n]))
        return ans