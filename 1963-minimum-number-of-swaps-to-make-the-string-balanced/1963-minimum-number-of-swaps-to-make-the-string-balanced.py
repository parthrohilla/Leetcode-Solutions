class Solution:
    def minSwaps(self, s: str) -> int:
        stack, swap = 0, 0
        for char in s:
            if char == "[":
                stack += 1
            else:
                if stack == 0:
                    swap += 1
                    stack += 1
                else:
                    stack -= 1
        return swap