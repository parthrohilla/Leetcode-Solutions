class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count, res = [0]*n, [0]*n
        def postorder(i, parent = -1):
            for nei in adj[i]:
                if nei == parent: 
                    continue
                else:
                    postorder(nei,i)
                    count[i] += count[nei]
                    res[i] += (res[nei] + count[nei])
            count[i] += 1
        
        def preorder(i, parent = -1):
            for nei in adj[i]:
                if nei == parent:
                    continue
                else:
                    res[nei] = res[i] - count[nei] + (len(count)-count[nei])
                    preorder(nei,i)
        
        postorder(0)
        preorder(0)
        return res
                
        
        
        
        
        