class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = (Counter(s))
        b = (Counter(t))
        return sum((a-b).values())