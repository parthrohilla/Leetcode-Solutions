class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1: return list(words[0])
        setA, setB = [0]*26, [0]*26
        
        wordA, wordB = words[0], words[1]
        for char in wordA: setA[ord(char)-ord("a")] += 1
        for char in wordB: setB[ord(char)-ord("a")] += 1
            
        #intersection of sets
        for i in range(26):
            if setA[i] != setB[i]: setA[i] = setB[i] = min(setA[i],setB[i])
        
        for i in range(2,len(words)):
            setB = [0]*26
            for char in words[i]: setB[ord(char)-ord("a")] += 1
            for i in range(26):
                   if setA[i] != setB[i]:
                        setA[i] = setB[i] = min(setA[i],setB[i])
        
        ans = []
        for i in range(26):
            if setA[i] != 0:
                ans += [(chr(ord("a") + i))]*setA[i]
        return ans
                
            
            
            