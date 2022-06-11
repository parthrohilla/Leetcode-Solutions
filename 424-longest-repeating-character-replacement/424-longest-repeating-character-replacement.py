class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        
        res = 0
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            
            while (r-l+1)-max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res