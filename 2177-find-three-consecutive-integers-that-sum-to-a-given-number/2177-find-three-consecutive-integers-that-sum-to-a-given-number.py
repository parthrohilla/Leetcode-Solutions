class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num - 3) // 3
        res = [x, x+1, x+2]
        return res if sum(res) == num else []