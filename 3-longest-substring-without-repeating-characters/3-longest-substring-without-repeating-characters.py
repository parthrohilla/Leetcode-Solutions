class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, maxLength = 0, 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            else:
                charSet.add(s[r])
                maxLength = max(maxLength, r-l+1)
                r += 1
        
        return maxLength