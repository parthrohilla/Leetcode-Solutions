class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(heap) < k:
                    heapq.heappush(heap, -1 * matrix[i][j])
                else:
                    if matrix[i][j] < -1 * heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -1 * matrix[i][j])
        
        return -1*heappop(heap)