class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(x):
            if x == 1: return "1"
            prev = helper(x-1)
            count, res = 1, ""
            for i in range(len(prev)):
                if (i + 1) < len(prev) and prev[i] == prev[i+1]: count += 1
                else:
                    res += str(count) + str(prev[i])
                    count = 1
            return res
        return helper(n)