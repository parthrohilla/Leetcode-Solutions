class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))
        
        for i, d in enumerate(n):
            if d == "6":
                n[i] = "9"
                break
        
        return int("".join(n))
            
        