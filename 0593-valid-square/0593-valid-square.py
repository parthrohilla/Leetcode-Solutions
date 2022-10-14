class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        
        distances = [self.length(p1,p2), self.length(p2,p3), self.length(p3,p4), self.length(p4,p1), self.length(p1,p3), self.length(p2,p4)]
        distances.sort()
        
        if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]:
            return True
        else:
            return False
                        
    def length(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    