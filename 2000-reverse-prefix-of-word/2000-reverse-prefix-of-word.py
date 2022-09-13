class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i,char in enumerate(word):
            if char == ch: 
                prefix = word[:i+1][::-1]
                return prefix + word[i+1:]
        return word