class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        arr = [x for x in arr if len(x) == len(set(x))]
        for i in range(1, len(arr)+1):
            strings = combinations(arr, i)
            for s in strings:
                temp = "".join(list(s))
                if len(temp) == len(set(temp)):
                    ans = max(ans, len(temp))
        return ans