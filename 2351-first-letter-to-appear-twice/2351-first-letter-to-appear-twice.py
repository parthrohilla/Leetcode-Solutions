class Solution:
    def repeatedCharacter(self, s: str) -> str:
        bitmap = 0
        for char in s:
            p = ord(char)-ord("a")
            bitmap ^= 1 << (ord(char)-ord("a"))
            if bitmap & (1<<p) == 0:
                return char
            