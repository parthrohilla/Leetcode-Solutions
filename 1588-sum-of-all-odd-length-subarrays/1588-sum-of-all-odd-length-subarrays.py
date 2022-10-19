class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        self.s = 0
        n = len(arr)
        
        # def brute_force():
        #     #------ Brute - Force Solution ------
        #     for i in range(n):
        #          for j in range(i, n, 2):
        #             self.s += sum(arr[i:j+1])
        #     return self.s
        # return brute_force()
        
        for i, num in enumerate(arr):
            T = (i+1)*(n-i)
            odd_sub_arrays = (T+1) // 2
            self.s += num * odd_sub_arrays
        return self.s
        
        
        