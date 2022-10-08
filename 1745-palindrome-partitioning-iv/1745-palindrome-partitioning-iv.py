class Solution:
    def checkPartitioning(self, s: str) -> bool:
        
        @lru_cache(None)
        def help(new_s, n):
            
            if n == 1: return new_s == new_s[::-1]
            
            for i in range(len(new_s)-1):
                if new_s[:i+1] == new_s[:i+1][::-1] and help(new_s[i+1:], n-1): return True
                
        return help(s, 3)