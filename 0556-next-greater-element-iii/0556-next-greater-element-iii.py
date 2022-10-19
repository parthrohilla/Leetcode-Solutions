class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = [int(x) for x in str(n)]
        # Find the pivot index - the "dip" value starting from the right
        pivot = -1
        for i in range(len(num)-1, 0, -1):
            if num[i-1] < num[i]:
                pivot = i-1
                break
        # No Greater Number Possible
        if pivot == -1: return -1
        # Find the swap Index
        swap_index = len(num) - 1
        while swap_index > pivot:
            if num[swap_index] > num[pivot]:
                break
            else:
                swap_index -= 1
        # Sort in ascending order after the pivot index, since we have already swapped pivot with a higher number
        num[pivot], num[swap_index] = num[swap_index], num[pivot]
        num = num[:pivot+1] + sorted(num[pivot+1:])
        ans =  int("".join(map(str,num)))
        # Returning answer if it fits in 32-bit as specified in the problem
        if ans >= 2**31: 
            return -1
        else: 
            return ans