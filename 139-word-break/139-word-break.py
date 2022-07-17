class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        
        def dfs(string) -> bool:
            if len(string) == 0:
                return True
            if string in memo:
                return memo[string]
            
            for i in range(len(string)):
                left = string[:i+1]
                if left in wordDict:
                    if dfs(string[i+1:]):
                        memo[string] = True
                        return True
            
            memo[string] = False
            return False
        
        return dfs(s)
        