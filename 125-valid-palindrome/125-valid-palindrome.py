class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for char in s:
            if char.isalnum():
                x += char
        x = x.lower()
        return x == x[::-1]