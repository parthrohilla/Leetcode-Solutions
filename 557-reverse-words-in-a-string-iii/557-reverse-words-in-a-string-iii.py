class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i, word in enumerate(words):
            words[i] = word[::-1]
        return " ".join(words)