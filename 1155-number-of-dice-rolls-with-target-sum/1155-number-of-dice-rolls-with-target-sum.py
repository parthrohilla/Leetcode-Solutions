class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        val = [x for x in range(1,k+1)]
        lookup = {}
        def dfs(times, curr):
            if (times,curr) in lookup: return lookup[(times,curr)]
            if curr == target and times == n: return 1
            if times >= n or curr > target: return 0
            
            ans = 0
            for pick in val:
                ans += (dfs(times+1,curr + pick))
            lookup[(times,curr)] = ans
            return lookup[(times,curr)] % (10**9+7)
        return dfs(0,0)