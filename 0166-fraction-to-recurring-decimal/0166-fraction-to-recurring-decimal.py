class Solution:
    def fractionToDecimal(self, N: int, D: int) -> str:
        ans = ""
        
        if N == 0:
            return "0"
        
        if N*D < 0:
            ans += "-"
        
        N = abs(N)
        D = abs(D)
        
        q = N // D
        ans += str(q)
        rem = N % D
        
        if rem == 0:
            return ans
        
        ans += "."
        seen = {}
        
        while rem != 0:
            
            if rem in seen:
                i = seen[rem]
                return (ans[:i] + "(" + ans[i:] + ")")
            
            seen[rem] = len(ans)
            rem *= 10
            q = rem // D
            ans += str(q)
            rem = rem % D
    
        return ans