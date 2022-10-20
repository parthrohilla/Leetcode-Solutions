class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            if num % 2: nums[i] = 1
            else: nums[i] = 0
        
        hashmap = {}
        prefix = 0
        hashmap[prefix] = 1
        ans = 0
        for i, num in enumerate(nums):
            prefix += num
            if (prefix - k) in hashmap:
                ans += hashmap[prefix-k]
            hashmap[prefix] = 1 + hashmap.get(prefix, 0)
        return ans
        