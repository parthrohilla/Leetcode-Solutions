class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        seen = {}
        ans = 0
        while r < n:
            seen[s[r]] = 1 + seen.get(s[r], 0)
            if len(seen.keys()) == 3:
                ans += (n - r)
            
            while len(seen.keys()) == 3:
                char = s[l]
                seen[char] -= 1
                if seen[char] == 0:
                    del seen[char]  
                else:
                    ans += (n - r)
                l += 1
            
            r += 1
        return ans
            
            
            