class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0
        for i in range(len(s)):
            freq = [0]*26
            for j in range(i, len(s)):
                lf = math.inf
                freq[ord(s[j]) - ord("a")] += 1
                mf = max(freq)
                for f in freq:
                    if 0 < f < lf:
                        lf = f
                        
                beauty += (mf-lf)
        return beauty
                