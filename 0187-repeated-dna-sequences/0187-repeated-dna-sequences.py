class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans, seen = [], set()
        for i in range(len(s)-9):
            dna_sequence = s[i:i+10]
            if dna_sequence in seen: ans.append(dna_sequence)
            else: seen.add(dna_sequence)
        return list(set(ans))