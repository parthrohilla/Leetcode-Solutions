class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num):
            reverse_i = int(str(i)[::-1])
            if i + reverse_i == num: return True
        return False if num else True