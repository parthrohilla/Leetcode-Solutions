class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        D = Counter(chars)
        ans = 0
        
        for word in words:
            temp = dict(D)
            good = True
            for char in word:
                if char not in temp: 
                    good = False
                    break
                else:
                    temp[char] -= 1
                    if temp[char] == 0:
                        del temp[char]
            if good:
                ans += len(word)
        
        return ans
            