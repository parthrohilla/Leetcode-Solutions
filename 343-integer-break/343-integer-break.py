class Solution:
    def integerBreak(self, n: int) -> int:
        integers = [i for i in range(1,n)]
        lookup = {}
        def dfs(i, s):
            if s == 0: return 1
            if i == 0: return integers[0]
            if (i,s) in lookup: return lookup[(i,s)]
            notpick = dfs(i-1,s)
            pick = -1
            if s - integers[i] >= 0:
                pick = integers[i] * dfs(i,s-integers[i])
            lookup[(i,s)] = max(pick, notpick)
            return lookup[(i,s)]
        
        return dfs(len(integers)-1,n)
        