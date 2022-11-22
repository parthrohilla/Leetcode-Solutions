class Solution:
    def minSteps(self, s: str, t: str) -> int:
        S, T = Counter(s), Counter(t)
        return sum((S-T).values()) + sum((T-S).values())