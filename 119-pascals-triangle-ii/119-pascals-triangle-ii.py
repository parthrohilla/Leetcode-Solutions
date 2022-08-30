class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        
        small = self.getRow(n-1)
        small = [0] + small + [0]
        ans = []
        for i in range(len(small)-1):
            ans.append(small[i] + small[i+1])
        return ans