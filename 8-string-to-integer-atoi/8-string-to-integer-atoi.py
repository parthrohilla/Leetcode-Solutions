class Solution(object):
    def myAtoi(self, s):
        ls = list(s.strip())
        if len(ls) == 0: 
            return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in '-+': 
            ls = ls[1:]
        
        ans = 0
        for symb in ls:
            if not symb.isdigit(): 
                break
            ans = ans*10 + int(symb)
        
        return max(-2**31, min(sign*ans, 2**31-1))