class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        n = len(A)
        A.sort(reverse = True)
        for i in range(n-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0