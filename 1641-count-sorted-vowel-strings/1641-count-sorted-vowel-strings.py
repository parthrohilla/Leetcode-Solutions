class Solution:
    def countVowelStrings(self, n: int) -> int:
        memo = {}
        def dfs(i,length):
            if length == n: return 1
            if i == 5: return 0
            if (i,length) in memo: return memo[(i,length)]
            unpick = dfs(i+1, length)
            pick = dfs(i, length+1)
            memo[(i,length)] = pick + unpick
            return memo[(i,length)]
        return dfs(0,0)