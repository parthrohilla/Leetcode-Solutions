class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = {}

        # populate the hashMap
        for task in tasks:
            hash_map[task] = 1 + hash_map.get(task, 0)

        # heapify list ie converting list to heap
        max_heap = [-x for x in hash_map.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0
        while max_heap or q:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
        