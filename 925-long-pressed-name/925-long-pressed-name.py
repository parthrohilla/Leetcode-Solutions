class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        if len(name) > len(typed):
            return False
        
        while j < len(typed):
            if i >= len(name):
                break
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif i>0 and j>0 and typed[j] == name[i-1]:
                j += 1
            else:
                return False
        
        if i != len(name):
            return False
        
        while j < len(typed):
            char = name[-1]
            if char != typed[j]:
                return False
            else:
                j += 1
        
        return True