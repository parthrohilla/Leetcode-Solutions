class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        C = Counter(arr)
        return len(C.values()) == len(set(C.values()))