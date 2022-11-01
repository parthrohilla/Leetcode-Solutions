class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        
        total, reductions, reduced_sum = sum(heap), 0, 0
        while reduced_sum < -total/2:
            biggest = heapq.heappop(heap)
            heapq.heappush(heap, biggest/2)
            reduced_sum += (-biggest/2)
            reductions += 1
            
        return reductions