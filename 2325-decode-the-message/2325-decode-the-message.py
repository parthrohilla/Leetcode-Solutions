class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen, k, mapping, output = set(), "", {" ": " "}, ""
        for char in key:
            if char not in seen and char != " ":
                k += char
                seen.add(char)
                
        for i in range(26):
            if k[i] not in mapping:
                mapping[k[i]] = chr(ord("a") + i)
        
        for char in message: 
            output += mapping[char]
        
        return output