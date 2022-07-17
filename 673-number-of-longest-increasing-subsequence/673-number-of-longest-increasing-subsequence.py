class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        maxLen, ans = 0, 0
        
        for i in range(len(nums)-1, -1, -1):
            tempLIS, tempCount = 1, 1
            for j in range(i+1, len(nums)):
                if nums[j] >  nums[i]:
                    lenLIS, count = dp[j]
                    if 1 + lenLIS > tempLIS:
                        tempLIS = 1 + lenLIS
                        tempCount = count 
                    elif 1 + lenLIS == tempLIS:
                        tempCount += count
            if tempLIS > maxLen:
                maxLen = tempLIS
                ans = tempCount
            elif tempLIS == maxLen:
                ans += tempCount
            
            dp[i] = [tempLIS, tempCount]
        
        return ans
                    
                    
                        
                