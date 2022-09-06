class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [x for x in range(26)]
        
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            p1 = find(ord(a)-ord("a"))
            p2 = find(ord(b)-ord("a"))
            
            if p1 == p2: return
            else: parent[p2] = p1
        
        # Union Step for equality equations
        for eq in equations:
            if eq[1:-1] == "==":
                union(eq[0], eq[-1])
        
        for eq in equations:
            if eq[1:-1] == "!=":
                a,b = ord(eq[0])-ord("a"), ord(eq[-1])-ord("a")
                if find(a) == find(b):
                    return False
        return True
        
        
        
        
        
                
                