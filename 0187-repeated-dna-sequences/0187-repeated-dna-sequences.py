class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashset = defaultdict(int)
        for i in range(len(s)-9):
            hashset[s[i:i+10]] += 1
        count = max(hashset.values()) if hashset else 0
        ans = []
        for key in hashset:
            if count > 1 and hashset[key] == count:
                ans.append(key)
        return ans