class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(a):
            if len(a) == 1: 
                return [[a[0]]]
            small = dfs(a[1:])
            ans = []
            for subset in small:
                for position in range(len(subset)+1):
                    ans.append(subset[:position] + [a[0]] + subset[position:])
            return ans
        temp = dfs(nums)
        seen = set()
        res = []
        for subset in temp:
            if tuple(subset) not in seen:
                res.append(subset)
                seen.add(tuple(subset))
        return res