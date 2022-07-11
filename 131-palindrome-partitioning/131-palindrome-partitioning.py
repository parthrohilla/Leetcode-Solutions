class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        part = []

        def dfs(i):
            if i >= len(s):
                output.append(part.copy())

            for j in range(i, len(s)):
                prefix = s[i:j+1]
                if self.isPalindrome(prefix):
                    part.append(prefix)
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return output

    def isPalindrome(self, string):
        left, right = 0, len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        