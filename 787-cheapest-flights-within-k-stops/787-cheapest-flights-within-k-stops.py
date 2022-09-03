class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0
        
        for _ in range(k+1):
            tmp_prices = prices.copy()
            for a,b,weight in flights:
                if prices[a]==math.inf:
                    continue
                if prices[a] + weight < tmp_prices[b]:
                    tmp_prices[b] = prices[a] + weight
            prices = tmp_prices
        return prices[dst] if prices[dst] != math.inf else -1
                    