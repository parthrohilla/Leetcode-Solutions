class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                ans += c
        
        l, r = 0, minutes
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        
        temp = extra
        while r < len(customers):
            if grumpy[r] == 1:
                temp += customers[r]
            if grumpy[l] == 1:
                temp -= customers[l]
            l += 1
            r += 1
            extra = max(extra, temp)
        return ans + extra