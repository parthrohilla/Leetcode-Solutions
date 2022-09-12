class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict(Counter(s))
        ans = 0
        print(count)
        flag = False
        for k,value in count.items():
            if value % 2 == 0:
                ans += value
            else:
                ans += (value-1)
                flag = True
                
        if flag: ans += 1
        return ans