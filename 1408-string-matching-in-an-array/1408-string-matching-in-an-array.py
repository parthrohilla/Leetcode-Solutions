class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        string = " ".join(words)
        return [x for x in words if string.count(x) >= 2]
            