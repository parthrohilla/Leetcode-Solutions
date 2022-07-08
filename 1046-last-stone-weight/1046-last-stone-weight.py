class Solution:
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1 and len(stones) != 0:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            remaining = abs(a-b)
            if remaining != 0:
                heapq.heappush(stones, -remaining)
                
        return -stones[0] if len(stones) != 0 else 0
        