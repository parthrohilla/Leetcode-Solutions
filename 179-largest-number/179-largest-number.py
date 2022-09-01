class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        def comparator(x,y):
            if x+y > y+x:
                return -1
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(comparator))
        return str(int("".join(nums)))