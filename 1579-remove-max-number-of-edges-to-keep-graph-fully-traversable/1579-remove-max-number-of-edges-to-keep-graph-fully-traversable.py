class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(parent, x):
            if parent[x] == x: return x
            parent[x] = find(parent,parent[x])
            return parent[x]
        
        def union(parent,n1,n2):
            p1,p2 = find(parent,n1), find(parent,n2)
            if p1 == p2: 
                return True
            else:
                parent[p2] = p1
                return False
            
        edges.sort(reverse=True)
        A,B = n,n
        parentA, parentB = [x for x in range(n+1)], [x for x in range(n+1)]
        remove = 0
        for t,a,b in edges:
            if t == 3:
                op1 = union(parentA,a,b)
                op2 = union(parentB,a,b)
                if op1 and op2:
                    remove += 1
                else:
                    A -= 1
                    B -= 1     
            elif t == 1:
                if union(parentA,a,b):
                    remove += 1
                else:
                    A -= 1
            else:
                if union(parentB,a,b):
                    remove += 1
                else:
                    B -= 1
                    
        print(A,B)   
        return remove if A == 1 and B == 1 else -1
                