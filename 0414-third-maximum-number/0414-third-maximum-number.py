class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = -math.inf, -math.inf, -math.inf
        for n in nums:
            if n in [first, second,third]:
                continue
            elif n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
        return third if third != -math.inf else first
                
                