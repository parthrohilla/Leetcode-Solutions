class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output, wordDict = [], set(wordDict)
        def dfs(string, current):
            if not string:
                output.append(current[:-1])
                return     
            for i in range(len(string)):
                left = string[:i+1]
                if left in wordDict:
                    dfs(string[i+1:], current + left + " ") 
            return    
        
        dfs(s, "")
        return output