class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for K,V in sorted(Counter(arr).items(), reverse = True):
            if K == V:
                return K
        return -1