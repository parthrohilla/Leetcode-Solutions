class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans, i = 0, 1
        for _ in range(len(piles) // 3):
            ans += piles[i]
            i += 2
            
        return ans