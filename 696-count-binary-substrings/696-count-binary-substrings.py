class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr_group, prev_group, ans = 1, 0, 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curr_group += 1
            else:
                ans += min(curr_group, prev_group)
                prev_group = curr_group
                curr_group = 1
        return ans + min(curr_group,prev_group)