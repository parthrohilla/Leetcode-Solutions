class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s): return False
        goal = goal*2
        return s in goal