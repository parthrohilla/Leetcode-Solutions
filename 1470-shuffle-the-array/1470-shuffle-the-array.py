class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        l, r = 0, n
        i = 0
        while r<len(nums):
            if i%2 == 0:
                ans.append(nums[l])
                i += 1
                l += 1
            else:
                ans.append(nums[r])
                i += 1
                r += 1
        return ans