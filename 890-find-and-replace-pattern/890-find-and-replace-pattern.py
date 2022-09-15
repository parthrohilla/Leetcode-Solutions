class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            flag = True
            seen = {}
            for i in range(len(pattern)):
                if pattern[i] in seen:
                    if word[i] != seen[pattern[i]]:
                        flag = False
                        break
                else:
                    if word[i] in seen.values(): 
                        flag = False
                        break
                    seen[pattern[i]] = word[i]
            if flag:
                ans.append(word)
        return ans
                    