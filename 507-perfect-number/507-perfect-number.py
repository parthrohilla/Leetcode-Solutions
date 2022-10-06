class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        k = 1
        i = 2
        while i < pow(num,0.5):
            if num % i == 0:
                k += i + (num//i)
            i += 1
        
        if pow(num,0.5)**2 == num: k += i
        return k == num
        