class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        self.s = 0
        n = len(arr)
        # brute Force Solution O(n^2)
        def brute_force():
            for i in range(n):
                 for j in range(i, n, 2):
                    self.s += sum(arr[i:j+1])
            return self.s
        
        # optimal Solution - Counting the sub-arrays the current element is part of
        def optimal():
            for i, num in enumerate(arr):
                T = (i+1)*(n-i)
                odd_sub_arrays = (T+1) // 2
                self.s += num * odd_sub_arrays
            return self.s
        
        #return brute_force()
        return optimal()
        
        
    
    
        
        
        