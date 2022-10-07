class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        content = 0
        for j,value in enumerate(s):
            if i < len(g) and value >= g[i]:
                content += 1
                i += 1
        return content
        
        