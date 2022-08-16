class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return 0
        ans = 0
        
        def merge_tw0_sorted_arrays(a, b):
            i, j = 0, 0
            temp = []
            while i <len(a) and j < len(b):
                if a[i] < b[j]:
                    temp.append(a[i])
                    i += 1
                else:
                    temp.append(b[j])
                    j += 1
            if i < len(a):
                temp = temp + a[i:]
            if j < len(b):
                temp = temp + b[j:]
            return temp
            
        
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            
            left, right = mergesort(nums[:len(nums)//2]), mergesort(nums[len(nums)//2:])
            
            l, r = 0, 0
            while l < len(left) and r < len(right):
                nonlocal ans
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    ans += len(left) - l
                    r += 1
            return merge_tw0_sorted_arrays(left, right)
            
        
        print(mergesort(nums))
        return ans