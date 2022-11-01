class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            biggest_pile = heapq.heappop(heap)
            removed = -biggest_pile // 2
            new_pile = -biggest_pile - removed
            heapq.heappush(heap, -new_pile)
        
        return -sum(heap)
            