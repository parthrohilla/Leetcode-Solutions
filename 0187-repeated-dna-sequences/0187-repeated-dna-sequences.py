class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashset, ans = defaultdict(int), []
        
        for i in range(len(s)-9):
            hashset[s[i:i+10]] += 1
        
        
        for key in hashset:
            if hashset[key] > 1: ans.append(key)
        
        return ans