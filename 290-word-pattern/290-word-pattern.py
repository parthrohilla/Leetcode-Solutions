class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        seen = {}
        repeat = set()
        for i in range(len(s)):
            if s[i] not in seen:
                if pattern[i] in repeat:
                    return False
                seen[s[i]] = pattern[i]
                repeat.add(pattern[i])
            else:
                if seen[s[i]] != pattern[i]:
                    return False
        return True
                
        