class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        
        smallest = s
        for i in range(1,len(s)):
            temp = s[i:] + s[:i]
            smallest = min(smallest, temp)
        
        return smallest