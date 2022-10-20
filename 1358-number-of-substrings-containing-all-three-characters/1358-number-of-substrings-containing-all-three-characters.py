class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, l, r, seen, ans = len(s), 0, 0, {}, 0
        for r in range(n):
            # Acquire characters
            seen[s[r]] = 1 + seen.get(s[r], 0)
            
            if len(seen.keys()) == 3:
                ans += (n - r)
                # Releasing Characters until the required condition becomes False
                while len(seen.keys()) == 3:
                    char = s[l]
                    seen[char] -= 1
                    if seen[char] == 0: del seen[char]  
                    else: ans += (n - r)
                    l += 1
            
        return ans
            
            
            