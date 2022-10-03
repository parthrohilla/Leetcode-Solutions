class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = [[x] for x in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(output[i])<len(output[j])+1:
                    output[i] = output[j] + [nums[i]]
        return max(output,key=lambda x:len(x))
        