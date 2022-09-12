class Solution:
    def countAsterisks(self, s: str) -> int:
        temp = s.split("|")
        string = ""
        for i in range(0,len(temp),2):
            string += temp[i]
        
        return string.count("*")