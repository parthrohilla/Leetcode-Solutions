class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        s,p = 0, 1
        while temp:
            rem = temp % 10
            s += rem
            p *= rem
            temp = temp // 10
        return p-s