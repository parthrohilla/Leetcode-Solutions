class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x),x))
        
        def possible(word):
            i, j = 0, 0
            while i < len(s):
                if s[i] == word[j]: j += 1
                if j == len(word): return True
                i += 1
            return False
        
        for W in dictionary:
            if possible(W):
                return W
        return ""