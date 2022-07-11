class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = defaultdict(list)
        for string in strs:
            count = [0 for _ in range(26)]
            for char in string:
                count[ord(char)-ord("a")] += 1
            string_map[tuple(count)].append(string)
        
        return string_map.values()