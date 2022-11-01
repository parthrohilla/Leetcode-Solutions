class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(A, B):
            i, j, res = 0, 0, []
            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    res.append(A[i])
                    i += 1
                else:
                    res.append(B[j])
                    j += 1
            return res + A[i:] + B[j:]
        
        def mergesort(start, end):
            if start == end: return [nums[start]]
            m = (start+end)//2
            A, B = mergesort(start,m), mergesort(m+1,end)
            return merge(A, B)
        
        return mergesort(0, len(nums)-1)