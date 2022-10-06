class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, life1, life2 = 0,0,0,0
        
        for n in nums:
            if n == candidate1: life1 += 1
            elif n == candidate2: life2 += 1
            elif life1 == 0:
                candidate1 = n
                life1 = 1
            elif life2 == 0:
                candidate2 = n
                life2 = 1
            else:
                life1 -= 1
                life2 -= 1
        
        ans = []
        count1, count2 = 0, 0
        for n in nums:
            if n == candidate1: count1 += 1
            elif n == candidate2: count2 += 1
                
        if count1 > len(nums)//3: ans.append(candidate1)
        if count2 > len(nums)//3: ans.append(candidate2)
        return ans
        
        