class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        seen = set()
        for numerator in range(1,n):
            for denominator in range(numerator+1,n+1):
                if (numerator/denominator) < 1 and (numerator/denominator) not in seen:
                    ans.append(str(numerator) + "/" + str(denominator))
                    seen.add(numerator/denominator)
        return ans
            
                