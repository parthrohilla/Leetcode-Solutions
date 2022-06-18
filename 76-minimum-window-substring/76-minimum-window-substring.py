class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""
        if s == t: return s
        
        mapT = Counter(t)
        window = {}
        l, have, need = 0, 0, len(mapT)
        
        resLen, res = math.inf, ""
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            if char in mapT and window[char] == mapT[char]:
                have += 1
                
                while have == need:
                    if (r-l+1) < resLen:
                        resLen = r-l+1
                        res = s[l:r+1]
                        
                    window[s[l]] -= 1
                    if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                        have -= 1
                    
                    l += 1
                  
        return res
                    
                    
                    
                
        