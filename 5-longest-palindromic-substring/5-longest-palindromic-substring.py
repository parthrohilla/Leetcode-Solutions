class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            odd_palindromic = self.expand(i, i, s)
            even_palindromic = self.expand(i, i+1, s)
            temp = odd_palindromic if len(odd_palindromic) > len(even_palindromic) else even_palindromic
            if len(ans) < len(temp): ans = temp
        return ans
    
    def expand(self, l, r, string):
        temp = ""
        while l>=0 and r<len(string) and string[l] == string[r]:
            temp = string[l:r+1]
            l -= 1
            r += 1
        return temp
        
        