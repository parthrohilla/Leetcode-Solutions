class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == int(pow(num,0.5)) ** 2
            