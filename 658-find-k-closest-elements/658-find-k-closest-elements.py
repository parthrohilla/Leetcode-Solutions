class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for n in arr:
            heapq.heappush(heap, [abs(x-n),n])
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return sorted(ans)