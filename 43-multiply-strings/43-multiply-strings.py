class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0]*(len(num1)+len(num2))
        
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                res[i+j] = (res[i+j] + product)
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = res[i+j] % 10
        
        res = res[::-1]
        begin = 0
        while begin<len(res) and res[begin] == 0:
            begin += 1
        
        res = res[begin:]
        temp = [str(x) for x in res]
        return "".join(temp)
        
                