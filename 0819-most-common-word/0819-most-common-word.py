class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for i, char in enumerate(paragraph):
            if char in "!?',;.":
                paragraph = paragraph[:i] + " " + paragraph[i+1:]

        freq = Counter(paragraph.lower().split())
        for word in banned:
            del freq[word]
        
        return max(freq.keys(), key = lambda x: freq[x])