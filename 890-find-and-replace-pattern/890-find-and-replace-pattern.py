class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word):
            hashmap = {}
            encoding = []
            for char in word:
                encoding.append(hashmap.setdefault(char,len(hashmap)))
            return encoding
        
        x = encode(pattern)
        return [word for word in words if encode(word) == x]
                    