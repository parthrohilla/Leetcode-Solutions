class Solution:
    def interpret(self, s: str) -> str:
        ans = ""
        i = 0
        while i < len(s):
            if s[i] == "G":
                ans += "G"
                i += 1
            elif s[i:i+2] == "()":
                ans += "o"
                i += 2
            elif s[i:i+4] == "(al)":
                ans += "al"
                i += 4
        return ans