class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = digits[::-1]
        carry = 1
        
        for i,n in enumerate(arr):
            val = arr[i] + carry
            arr[i] = val % 10
            carry = val//10
        
        if carry == 1:
            arr.append(carry)
        
        return arr[::-1]