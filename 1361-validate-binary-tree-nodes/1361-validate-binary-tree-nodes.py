class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        adj, i = defaultdict(list), 0
        parent = [0]*n
        for l,r in zip(leftChild, rightChild):
            if l != -1: 
                parent[l] += 1
                adj[i].append(l)
                if parent[l] > 1: return False
            if r != -1: 
                parent[r] += 1
                adj[i].append(r)
                if parent[r] > 1: return False
            i += 1
        
        if len([x for x in parent if x == 0]) != 1:
            return False
        
        p = [x for x in range(n)]
        #union - find
        def find(x):
            if p[x] == x: return x
            p[x] = find(p[x])
            return p[x]
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return 0
            else:
                p[p2] = p1
                return 1
        
        components = n
        for i in adj.keys():
            for j in adj[i]:
                print(i,j)
                components -= union(i,j)
        
        
        if components == 1:
            return True
        else: 
            return False
        
        
        
        
