class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, mid = math.inf, math.inf
        for n in nums:
            if n < left: left = n
            elif n < mid and n > left: mid = n
            elif n > mid: return True
        return False