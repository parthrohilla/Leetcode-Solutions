class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        
        smallest = s
        for i in range(1,len(s)):
            smallest = min(smallest, s[i:] + s[:i])
        
        return smallest