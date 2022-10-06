class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([x for x in sorted(nums)[::2]])