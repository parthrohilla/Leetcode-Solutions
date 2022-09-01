class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m, seen = {}, set()
        for i in range(len(s)):
            if s[i] not in m:
                if t[i] in seen:
                    return False
                m[s[i]] = t[i]
                seen.add(t[i])
            else:
                if t[i] != m[s[i]]:
                    return False
        return True