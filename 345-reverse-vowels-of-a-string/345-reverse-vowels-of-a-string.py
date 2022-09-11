class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        seq = ""
        for char in s:
            if char in vowels:
                seq = char + seq
        
        j = 0
        ans = ""
        for char in s:
            if char not in vowels:
                ans += char
            else:
                ans += seq[j]
                j += 1
        return ans