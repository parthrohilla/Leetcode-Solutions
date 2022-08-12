class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str in strs:
            encode = [0]*26
            for ch in str:
                encode[ord(ch)-ord("a")] += 1
            encode = tuple(encode)
            group[encode].append(str)
        return group.values()
        