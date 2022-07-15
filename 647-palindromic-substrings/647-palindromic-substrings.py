class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def helper(left, right):
            nonlocal ans
            while left >= 0 and right < len(s) and s[left]==s[right]:
                ans += 1
                left -= 1
                right += 1
            
        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)
        return ans