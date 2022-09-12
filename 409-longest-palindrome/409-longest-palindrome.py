class Solution:
    def longestPalindrome(self, s: str) -> int:
        count, ans, odd = dict(Counter(s)), 0, False
        for k,value in count.items():
            if value % 2 == 0: 
                ans += value
            else:
                ans += (value-1)
                odd = True
                
        if odd: ans += 1
        return ans