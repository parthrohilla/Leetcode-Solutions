class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        sentence = [""]*(n+1)
        for word in words:
            k = int(word[-1])
            sentence[k] = word[:-1]
        return " ".join(sentence[1:])