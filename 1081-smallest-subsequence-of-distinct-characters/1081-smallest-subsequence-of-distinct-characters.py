class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited = [False]*26
        last = {}
        
        for i, char in enumerate(s):
            last[char] = i
        
        ans = []
        for i,char in enumerate(s):
            if visited[ord(char)-ord("a")]: 
                continue
            
            while ans and ans[-1] > char and last[ans[-1]] > i and not visited[ord(char)-ord("a")]:
                visited[ord(ans.pop()) - ord("a")] = False
                
            ans.append(char)
            visited[ord(char)-ord("a")] = True
            
        return "".join(ans)