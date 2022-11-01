class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        
        total = sum(heap)
        op = 0
        reduced = 0
        while reduced < -total/2:
            biggest = heapq.heappop(heap)
            heapq.heappush(heap, biggest/2)
            reduced += (-biggest/2)
            op += 1
            
        return op