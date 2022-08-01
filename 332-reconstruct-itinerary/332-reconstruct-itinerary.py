class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src :[] for src, destination in tickets}
        
        for src, dest in tickets:
            adj[src].append(dest)
            
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            for i, v in enumerate(adj[src]):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        res = ["JFK"]
        dfs("JFK")
        return res