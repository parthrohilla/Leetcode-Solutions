class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        self.parent = [0]*N
        for i in range(0,N,2):
            self.parent[row[i]] = row[i]
            self.parent[row[i+1]] = row[i]
        
        swap = 0
        for i in range(0,N,2):
            swap += self.union(i,i+1)
        return swap
    
    def find(self,x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        
        if p1 == p2: return 0
        else:
            self.parent[p2] = p1
            return 1