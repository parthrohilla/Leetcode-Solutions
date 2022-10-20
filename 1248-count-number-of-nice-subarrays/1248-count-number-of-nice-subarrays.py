class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Change odd Numbers to 1 ans Even Numbers to 0
        for i, num in enumerate(nums):
            if num % 2: nums[i] = 1
            else: nums[i] = 0
        # The problem now becomes subarray Sum Equals K 
        hashmap = {}
        ans = prefix = 0
        hashmap[prefix] = 1
        for i, num in enumerate(nums):
            prefix += num
            if (prefix - k) in hashmap:
                ans += hashmap[prefix-k]
            hashmap[prefix] = 1 + hashmap.get(prefix, 0)
        return ans
        