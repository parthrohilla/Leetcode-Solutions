class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third = "qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"
        ans = []
        for word in words:
            flag = True
            if word[0] in first:
                for char in word:
                    if char not in first:
                        flag = False
                        break
            elif word[0] in second:
                for char in word:
                    if char not in second:
                        flag = False
                        break
            else:
                for char in word:
                    if char not in third:
                        flag = False
                        break
            if flag: ans.append(word)
        return ans
                
                
            