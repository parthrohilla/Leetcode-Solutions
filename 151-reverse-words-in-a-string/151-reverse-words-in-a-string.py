class Solution:
    def reverseWords(self, s: str) -> str:
        i, n = 0, len(s)
        res = []
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            j = i+1
            while j < n and s[j] != " ":
                j += 1
            if i != n: res.append(s[i:j])
            i = j+1
        
        return " ".join(res[::-1])