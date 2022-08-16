class Solution:
    def minSwaps(self, s: str) -> int:
        closing, ans = 0, 0
        for char in s:
            if char == "]":
                closing += 1
            else:
                closing -= 1
            ans = max(ans, closing)
        return (ans+1)//2