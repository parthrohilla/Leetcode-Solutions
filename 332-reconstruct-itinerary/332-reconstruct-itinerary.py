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
            
            temp = adj[src]
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                
                #Backtrack
                adj[src].insert(i, v)
                res.pop()
            return False
        
        res = ["JFK"]
        dfs("JFK")
        return res