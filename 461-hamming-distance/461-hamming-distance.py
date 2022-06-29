class Solution:
    def hammingDistance(self, a: int, b: int) -> int:
        c = a ^ b
        ans = 0
        while c:
            c = c & (c-1)
            ans += 1
        return ans