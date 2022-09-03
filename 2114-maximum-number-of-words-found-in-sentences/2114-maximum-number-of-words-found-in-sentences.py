class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            l,r = 0,0
            count = 0
            while r<len(sentence):
                while r < len(sentence) and sentence[r] != " ":
                    r += 1
                count += 1
                l = r+1
                r = l
            ans = max(ans, count)
        return ans