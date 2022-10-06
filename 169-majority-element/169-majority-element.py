class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, life = 0,0
        for n in nums:
            if n == candidate: life += 1
            elif life == 0:
                candidate = n
                life = 1
            else:
                life -= 1
        return candidate