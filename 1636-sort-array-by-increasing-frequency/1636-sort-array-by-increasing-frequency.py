class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        C = Counter(nums)
        nums.sort(key = lambda x: (C[x],-x))
        return nums