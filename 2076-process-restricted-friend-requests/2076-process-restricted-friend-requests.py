class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            x, y = find(a), find(b)
            if x == y: return
            parent[y] = x
            
        parent = [x for x in range(n)]
        ans = []
        
        for (u,v) in requests:
            U, V = find(u), find(v)
            friendship = True
            for x,y in restrictions:
                X, Y = find(x), find(y)
                if set([X,Y]) == set([U,V]):
                    friendship = False
                    break
            
            ans.append(friendship)
            if friendship:
                union(u,v)
                
        return ans
            
                    