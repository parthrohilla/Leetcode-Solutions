class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        start, end, profit = zip(*sorted(zip(start, end, profit)))

        @functools.lru_cache(None)
        def helper(i):
            if i == len(start): return 0
            j = bisect_left(start, end[i])
            return max(helper(i+1), profit[i] + helper(j))

        return helper(0)
        