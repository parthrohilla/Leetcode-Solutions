class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] > amount[0] + amount[1]:
            return amount[2]
        else:
            s = sum(amount)
            if s % 2 == 0: return s//2
            else: return s//2 + 1