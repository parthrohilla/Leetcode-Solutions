class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        return (-a-1) * (-b-1)