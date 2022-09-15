class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(x for x,v in Counter(nums).items() if v == 1)