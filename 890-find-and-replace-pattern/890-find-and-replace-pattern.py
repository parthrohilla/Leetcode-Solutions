class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word):
            m = {}
            encoding = []
            for char in word:
                encoding.append(m.setdefault(char,len(m)))
            return encoding
        
        x = encode(pattern)
        return [word for word in words if encode(word) == x]
                    