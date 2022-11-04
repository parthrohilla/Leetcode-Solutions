class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels, seq = set("aeiouAEIOU"), ""
        # Get vowel sequence in reverse order
        for char in s:
            if char in vowels:
                seq = char + seq
        #Build answer using reversed vowel sequence
        ans, j = "", 0
        for char in s:
            if char not in vowels: ans += char
            else:
                ans += seq[j]
                j += 1
        return ans