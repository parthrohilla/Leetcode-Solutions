class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0]*n
        for a,b in roads:
            deg[a] += 1
            deg[b] += 1
        
        imp = []
        for i,val in enumerate(deg):
            imp.append([val,i])
        imp.sort(reverse = True)
        
        k = n
        values = [0]*n
        for val,i in imp:
            values[i] = k
            k -= 1
        
        ans = 0
        for a,b in roads:
            ans += (values[a] + values[b])
        return ans