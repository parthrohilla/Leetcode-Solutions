class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        self.count = 0
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
                        self.count += 1
        
        return self.count