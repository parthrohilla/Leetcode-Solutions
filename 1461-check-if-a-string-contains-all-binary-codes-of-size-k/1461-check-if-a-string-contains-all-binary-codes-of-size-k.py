class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
            if len(seen) == 2**k:
                break
        
        temp = set()
        for string in seen:
            x = string[::-1]
            i, t=0, 0
            while i<k:
                t += (int(x[i]) * (2**i))
                i += 1
            temp.add(t)
        
        for i in range(2**k):
            if i not in temp:
                return False
        return True
                