class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = [0] * ( max(len(num1), len(num2)) + 1 )
        num1, num2 = num1[::-1], num2[::-1]
        
        i, j, k, carry = 0, 0, 0, 0
        while i < len(num1) and j < len(num2):
            temp = int(num1[i]) + int(num2[j]) + carry
            carry = temp // 10
            res[k] = temp % 10
            i += 1
            j += 1
            k += 1
        
        while i < len(num1):
            temp = int(num1[i]) + carry
            carry = temp // 10
            res[k] = temp % 10
            i += 1
            k += 1
        
        while j < len(num2):
            temp = int(num2[j]) + carry
            carry = temp // 10
            res[k] = temp % 10
            j += 1
            k += 1
        
        if carry:
            res[k] = 1
        
        res = res[::-1]
        if res[0] == 0:
            res = res[1:]
        
        res = [str(x) for x in res]
        return "".join(res)
            
        
        