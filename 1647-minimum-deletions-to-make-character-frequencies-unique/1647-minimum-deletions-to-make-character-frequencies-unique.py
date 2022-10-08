class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26
        for char in s:
            freq[ord(char)-ord("a")] += 1
        
        unique = set()
        deletions = 0
        for n in freq:
            count = n
            while count and count in unique:
                deletions += 1
                count -= 1
            
            if count:
                unique.add(count)
        return deletions
                
                
                
                
        
            
        
            