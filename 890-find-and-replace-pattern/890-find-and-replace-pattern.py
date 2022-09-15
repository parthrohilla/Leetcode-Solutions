class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def p(word):
            m = {}
            encoding = []
            for char in word:
                encoding.append(m.setdefault(char,len(m)))
            return encoding
        
        return [word for word in words if p(word) == p(pattern)]
                    