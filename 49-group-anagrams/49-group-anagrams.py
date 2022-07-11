class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for string in strs:
            count = [0 for _ in range(26)]
            for char in string:
                count[ord(char)-ord("a")] += 1

            key = tuple(count)
            if key not in string_map:
                string_map[key] = []
            string_map[key].append(string)

        return string_map.values()