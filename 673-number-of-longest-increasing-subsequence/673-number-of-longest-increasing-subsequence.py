class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        maxLIS,maxcount = 0,0
        for i in range(len(nums)-1,-1,-1):
            tempLIS, countLIS = 1,1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    LIS,count = dp[j]
                    if 1 + LIS > tempLIS:
                        tempLIS = 1 + LIS
                        countLIS = count
                    elif 1 + LIS == tempLIS:
                        countLIS += count
            if tempLIS > maxLIS:
                maxLIS = tempLIS
                maxcount = countLIS
            elif tempLIS == maxLIS:
                maxcount += countLIS
            dp[i] = [tempLIS,countLIS]
        return maxcount
                