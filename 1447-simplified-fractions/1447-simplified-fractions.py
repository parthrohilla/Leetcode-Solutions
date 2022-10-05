class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        seen = set()
        for a in range(1,n):
            for d in range(2,n+1):
                if (a/d) < 1 and (a/d) not in seen:
                    ans.append(str(a) + "/" + str(d))
                    seen.add(a/d)
        return ans
            
                