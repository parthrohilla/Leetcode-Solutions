class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(x):
            if x == 1: return "1"
            prev = rec(x-1)
            
            count = 1
            res = ""
            for i in range(len(prev)):
                if i + 1 < len(prev) and prev[i] == prev[i+1]:
                    count += 1
                else:
                    res += str(count) + str(prev[i])
                    count = 1
            return res
        
        return rec(n)