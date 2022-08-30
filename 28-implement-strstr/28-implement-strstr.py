class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        for i, char in enumerate(haystack):
            if char == needle[0] and haystack[i:i+n] == needle:
                    return i
        return -1