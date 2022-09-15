class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(key for key,v in Counter(nums).items() if v == 1)