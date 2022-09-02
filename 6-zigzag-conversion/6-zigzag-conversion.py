class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1 or n>=len(s):
            return s
        
        arr = [[] for _ in range(n)]
        directions = -1
        row = 0
        for char in s:
            arr[row].append(char)
            if row == 0 or row == n-1:
                directions *= -1
            row += directions
        
        ans = ""
        for a in arr:
            ans += "".join(a)
        return ans
        
        
        
        