class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for n in nums:
            bits = bits | n
        return bits << (len(nums)-1)