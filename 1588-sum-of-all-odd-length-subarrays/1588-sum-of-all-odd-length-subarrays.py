class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        for i in range(n):
            for j in range(i, n, 2):
                s += sum(arr[i:j+1])
        return s