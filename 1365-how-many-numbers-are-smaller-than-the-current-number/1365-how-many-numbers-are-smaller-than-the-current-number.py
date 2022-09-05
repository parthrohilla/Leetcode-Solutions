class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0]*(101)
        for n in nums:
            bucket[n] += 1
        ans = [0]*(101)
        temp = 0
        for i,n in enumerate(bucket[:-1]):
            temp += n
            ans[i+1] = temp
        return [ans[i] for i in nums]