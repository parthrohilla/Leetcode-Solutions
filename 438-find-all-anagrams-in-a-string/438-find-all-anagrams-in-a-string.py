class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        k = len(p)
        chars_p = {}
        for char in p:
            chars_p[char] = chars_p.get(char,0) + 1
        
        chars_s = {}
        for i in range(k):
            chars_s[s[i]] = chars_s.get(s[i],0) + 1
        
        l,r = 0, k
        ans = []
        
        if chars_s == chars_p:
                ans.append(l)
        
        while r<len(s):
            chars_s[s[r]] = chars_s.get(s[r],0) + 1
            if chars_s[s[l]] == 1:
                del chars_s[s[l]]
            else:
                chars_s[s[l]] -= 1
            
            if chars_s == chars_p:
                ans.append(l+1)
            
            l+=1
            r+=1
        return ans
            