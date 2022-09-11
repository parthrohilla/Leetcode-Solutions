class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for char in magazine: freq[char] = freq.get(char,0) + 1
            
        for char in ransomNote:
            if char not in freq:
                return False
            else:
                freq[char] -= 1
                if freq[char] == 0:  del freq[char]
        return True