class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        
        while l<=r:
            mid = (l+r) // 2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return l