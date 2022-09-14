class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal:
            if len(s) == len(set(s)):return False
            return True
        
        s = list(s)
        goal = list(goal)
        
        i,first,second = 0,-1,-1
        while i < len(s):
            if s[i] != goal[i]:
                if first == -1:
                    first = i
                else:
                    second = i
                    break
            i += 1
        
        s[first],s[second] = s[second],s[first]
        if s == goal: return True
        return False
