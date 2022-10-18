class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums1): 
            hashmap[num] = i
        
        ans, stack = [-1]*len(nums1), []
        for num in nums2:
            while stack and stack[-1] < num:
                pop = stack.pop()
                if pop in hashmap:
                    ans[hashmap[pop]] = num
            stack.append(num)
        
        return ans