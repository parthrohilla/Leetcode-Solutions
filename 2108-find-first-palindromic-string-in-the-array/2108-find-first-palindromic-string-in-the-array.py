class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for string in words:
            if string == string[::-1]:
                return string
        return ""