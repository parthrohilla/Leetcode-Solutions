class Solution:
    def minSteps(self, s: str, t: str) -> int:
        A = Counter(s)
        B = Counter(t)
        return sum((A-B).values()) + sum((B-A).values())