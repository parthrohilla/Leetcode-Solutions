class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count, total, odd = Counter(words), 0, 0
        
        for word in count.keys():
            
            if word[0] == word[1]:
                total += (count[word]//2) * 2 * 2
                odd = max(odd, (count[word] % 2) * 2)
            
            elif word[::-1] in count:
                total += min(count[word], count[word[::-1]]) * 2
        
        return total + odd