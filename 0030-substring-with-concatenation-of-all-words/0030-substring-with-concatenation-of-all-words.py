class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq, k, ans = dict(Counter(words)), len(words[0]), []
        
        for i in range(len(s)- k*len(words)+1):
            copyMap = freq.copy()
            for j in range(i, i + k*len(words), k):
                w = s[j:j+k]
                if w in copyMap:
                    if copyMap[w] == 1: del copyMap[w]
                    else: copyMap[w] -= 1
                    if not copyMap: ans.append(i)
                else:
                    break    
        return ans