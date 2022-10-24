class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def convert(event):
            return int(event[:2])*60 + int(event[-2:])
        
        e1_start, e1_end = convert(event1[0]), convert(event1[1])
        e2_start, e2_end = convert(event2[0]), convert(event2[1])
        
        if e1_start < e2_start and e1_end >= e2_start: return True
        elif e2_start < e1_start and e2_end >= e1_start: return True
        else: return False