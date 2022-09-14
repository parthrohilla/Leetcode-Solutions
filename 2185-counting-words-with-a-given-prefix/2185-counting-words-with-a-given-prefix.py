class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 if word[:len(pref)] == pref else 0 for word in words)