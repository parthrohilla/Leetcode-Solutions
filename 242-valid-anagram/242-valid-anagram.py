class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}
        for ch in s:
            map_s[ch] = 1 + map_s.get(ch,0)
        for ch in t:
            map_t[ch] = 1 + map_t.get(ch,0)
        return map_s == map_t