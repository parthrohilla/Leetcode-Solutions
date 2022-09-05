class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = [0]*101
        for n in nums:
            count[n] += 1
        ans = 0
        for i in range(k+1, 101):
            ans += (count[i] * count[i-k])
        return ans