class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        A = sorted(nums)[::-1]
        for i in range(n-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0