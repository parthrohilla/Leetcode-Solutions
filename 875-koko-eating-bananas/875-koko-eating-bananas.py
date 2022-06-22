class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        k = r
        while l<=r:
            mid = int((l+r)/2)
            tempAns = self.helper(piles, mid)
            if tempAns <= h:
                k = min(k, mid)
                r = mid-1
            else:
                l = mid+1
        return k
    
    def helper(self, piles, n):
        ans = 0
        for num in piles:
            ans += math.ceil(num/n)
        return ans
        