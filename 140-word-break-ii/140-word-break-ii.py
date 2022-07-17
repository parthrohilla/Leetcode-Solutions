class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = defaultdict(list)
        
        def dfs(string) -> List[str]:
            if string in memo:
                return memo[string]
            
            res = []
            for i in range(len(string)):
                left = string[:i+1]
                if left in wordDict:
                    if left == string:
                        res.append(left)
                    else:
                        small = dfs(string[i+1:])
                        for x in small:
                            res.append(left + " " + x)                      
            
            memo[string] = res        
            return res
        
        return dfs(s)