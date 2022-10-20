class Solution:
    def countVowels(self, word: str) -> int:
        n, ans, vowels = len(word), 0, set("aeiou")
        for i, char in enumerate(word):
            if char in vowels:
                T = (i+1) * (n-i)
                ans += T
        return ans
                