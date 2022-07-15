class Solution:
    def validPalindrome(self, s: str) -> bool:
        removed_flag = False
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                if s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                elif s[l:r] == s[l:r][::-1]:
                    return True
                else:
                    return False
            else:
                l += 1
                r -= 1
        
        return True
                
            