class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        for emails in accounts:
            for i in range(2,len(emails)):
                adj[emails[i]].append(emails[i-1])
                adj[emails[i-1]].append(emails[i])
        
        def dfs(email):
            seen.add(email)
            res = [email]
            small = []
            for u in adj[email]:
                if u not in seen:
                    small += dfs(u)
            return res + small
        
        seen = set()
        ans = []
        for emails in accounts:
            if emails[1] not in seen:
                ans.append([emails[0]] + sorted(dfs(emails[1])))
        return ans