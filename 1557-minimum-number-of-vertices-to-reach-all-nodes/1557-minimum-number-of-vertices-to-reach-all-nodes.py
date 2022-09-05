class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        deg = [0]*n
        for a,b in edges:
            deg[b] += 1
        
        ans = []
        for i in range(n):
            if not deg[i]: 
                ans.append(i)
        return ans