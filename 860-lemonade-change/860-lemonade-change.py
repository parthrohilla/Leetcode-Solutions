class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0, 10:0, 20:0}
        for bill in bills:
            change = 0
            if bill == 10: change = 5
            elif bill == 20: change = 15
            
            money[bill] += 1
            if change == 0:
                continue
            elif change == 5:
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            elif change == 15:
                if money[5] > 0 and money[10] > 0:
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] >= 3:
                    money[5] -= 3    
                else:
                    return False    
        return True
            