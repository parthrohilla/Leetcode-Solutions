class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map, s2Map = Counter(s1), {}
        
        for r in range(len(s2)):
            if s2[r] in s1Map:
                substring = s2[r:r + sum(s1Map.values())]
                if Counter(s1Map) == Counter(substring):
                    return True
            
        return False
        
        
            