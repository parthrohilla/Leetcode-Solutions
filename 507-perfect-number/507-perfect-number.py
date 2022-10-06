class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisor_sum, i = 1, 2
        while i < pow(num,0.5):
            if num % i == 0: divisor_sum += i + (num//i)
            i += 1
        if pow(num,0.5)**2 == num: divisor_sum += i
        return divisor_sum == num
        