class Solution:
     def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        count = 0

        def sort(a, b):
            temp = []
            i, j = 0, 0
            while i<len(a) and j <len(b):
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
            
            
        
        def merge(nums):
            if len(nums) <= 1: 
                return nums
            
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            l = r = 0
            
            while l < len(left) and r < len(right):
                nonlocal count
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    count += len(left) - l
                    r += 1
            return sort(left, right)

        merge(nums)
        return count
        