class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0
        
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord("a")] += 1
                most_frequenct = max(freq)
                least_frequent = math.inf
                
                for x in freq:
                    if 0 < x < least_frequent:
                        least_frequent = x      
                
                beauty += (most_frequenct - least_frequent)
        
        return beauty
                