class Solution:
    def subarraysWithKDistinct(self, nums: List[int], K: int) -> int:
        def atMostK(k):
            l = ans = 0
            count = {}
            for r, num in enumerate(nums):
                count[num] = 1 + count.get(num, 0)
                while len(count.keys()) == k+1:
                    left = nums[l]
                    count[left] -= 1
                    if count[left] == 0: 
                        del count[left]
                    l += 1
                ans += (r-l + 1)
            return ans
        
        return atMostK(K) - atMostK(K-1)