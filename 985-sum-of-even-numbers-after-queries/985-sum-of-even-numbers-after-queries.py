class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum([x for x in nums if x%2==0])
        ans = []
        
        for val, i in queries:
            temp = nums[i] + val
            if nums[i] % 2 == 0:
                if temp % 2 == 0:
                    ans.append(even+val)
                    even = even+val
                else:
                    ans.append(even-nums[i])
                    even = even - nums[i]
            else:
                if temp % 2 == 0:
                    ans.append(even+temp)
                    even = even+temp
                else:
                    ans.append(even)
            nums[i] = temp
        return ans