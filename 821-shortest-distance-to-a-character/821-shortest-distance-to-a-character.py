class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [math.inf if char != c else 0 for i,char in enumerate(s)]
        temp = math.inf
        for i,num in enumerate(ans):
            if num == 0: temp = 0
            else: ans[i] = min(ans[i], temp)
            temp += 1
        
        for i in range(len(ans)-1, -1, -1):
            num = ans[i]
            if num == 0: temp = 0
            else: ans[i] = min(ans[i], temp)
            temp += 1
        
        return ans
            