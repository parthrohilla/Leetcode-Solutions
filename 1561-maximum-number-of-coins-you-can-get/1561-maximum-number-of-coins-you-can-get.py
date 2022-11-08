class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        print(piles)
        
        ans = 0
        k = len(piles) // 3
        i = 1
        while k > 0:
            ans += piles[i]
            i += 2
            k -= 1
            
        return ans