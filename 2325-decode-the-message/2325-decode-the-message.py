class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k = ""
        seen = set()
        for char in key:
            if char not in seen and char != " ":
                k += char
                seen.add(char)
        mapping = {}
        j = 0
        for i in range(26):
            if k[i] not in mapping:
                mapping[k[i]] = chr(ord("a") + i)
        
        mapping[" "] = " "
        output = ""
        for char in message:
            output += mapping[char]
        return output